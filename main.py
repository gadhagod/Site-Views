from os import getenv, remove
from anybadge import Badge
from flask import Flask, request, render_template
from rockset import Client, Q, F
from time import sleep

rs = Client(api_key=getenv('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')
app = Flask(__name__, template_folder='js')
collection = rs.Collection.retrieve('RepoViews')

def make_badge(views, color='green'):
    badge = Badge('views', views, thresholds={
        views: color
    })

    try:
        remove('badge.svg')
    except FileNotFoundError:
        pass
    badge.write_badge('badge.svg')

@app.route('/text/<site>')
def get_upd_views(site):
    cnt = list(
        rs.sql(
            Q('SELECT * FROM commons.RepoViews WHERE _id=\'{}\''.format(site))
        )
    )

    if cnt == []:
        collection.add_docs([{
            '_id':site, 'views': 0
        }])
        return(get_upd_views(site))
    
    views = cnt[0]['views'] + 1

    collection.add_docs([{
        '_id':site, 'views': views
    }])    

    return(str(views))

@app.route('/badge/<site>')
def badge(site, args=False):
    if not args:
        args = request.args.to_dict()
    if 'color' in args.keys():
        make_badge(get_upd_views(site), color=args['color'])
    else:
        make_badge(get_upd_views(site))

    return(open('badge.svg', 'r').read())

@app.route('/js/text/<site>')
def js_txt(site):
    args = request.args.to_dict()
    if 'tag' in args.keys():
        tag = '<{}>'.format(args['tag'])
        end_tag = '</{}>'.format(args['tag'])
    else:
        tag = ''
        end_tag = ''
    return(render_template('add_text.js', views=get_upd_views(site), tag=tag, end_tag=end_tag))

@app.route('/js/badge/<site>')
def js_lib(site):
    args = request.args.to_dict()
    if 'center' in args.keys():
        if args['center'].lower() == 'true':
            align = '<center>'
            end_align = '</center>'
    else:
        align = ''
        end_align = ''
    return(render_template('add_badge.js', badge=badge(site, args), align=align, end_align=end_align).replace('\n', ''))