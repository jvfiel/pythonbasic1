import facebook, os
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("{0}/fb.ini".format(os.path.dirname(os.path.abspath(__file__))))
#url = Config.get('fb', 'url', 0)

def renew_fb_token(graph):
    app_id = Config.get('fb', 'app_id', 0)
    app_secret = Config.get('fb', 'app_secret', 0)

    # Extend the expiration time of a valid OAuth access token.
    extended_token = graph.extend_access_token(app_id, app_secret)
    return extended_token  # verify that it expires in 60 days

#bench execute wela_mobile_connector.wela_mobile_connector.doctype.school_feeds.fb_api.test_post
def test_post():
    #sample_photo = frappe.get_site_path() + '/public' + frappe.db.get_value("Mobile Settings", None, "test_fb_photo")
    sample_photo = '/home/jvfiel/projects/pythonlegends/level11_fb/owl.jpg'
    img_list = [sample_photo]
    #msg = frappe.db.get_value("Mobile Settings", None, "test_fb_message_post")
    msg = "Hello World"
    post_feed(msg,img_list)

# bench execute wela_mobile_connector.wela_mobile_connector.doctype.school_feeds.fb_api.post_feed
def post_feed(msg, img_list):
    # Fill in the values noted in previous steps here

    # page_id = frappe.db.get_value("Mobile Settings", None, "fb_page_id")
    # page_access_token = frappe.db.get_value("Mobile Settings", None, "page_access_token")
    page_id = Config.get('fb', 'page_id', 0)
    page_access_token = Config.get('fb', 'page_access_token', 0)
    print 'has page access token', page_access_token
    api = facebook.GraphAPI(page_access_token)
    #print "expired old", page_access_token
    # page_access_token = renew_fb_token(page_access_token)
    page_access_token = renew_fb_token(api)
    renewed_token = page_access_token['access_token']
    print "renewed", page_access_token
    api = facebook.GraphAPI(renewed_token)
    #frappe.db.set_value("Mobile Settings", None, "page_access_token", renewed_token)

    imgs_id = []
    for img in img_list:
        photo = open(img, "rb")
        # print img
        imgs_id.append(api.put_photo(photo, album_id='me/photos', published=False)['id'])
        photo.close()

    args = dict()
    args["message"] = msg
    for img_id in imgs_id:
        key = "attached_media[" + str(imgs_id.index(img_id)) + "]"
        args[key] = "{'media_fbid': '" + img_id + "'}"

    status = api.request(path='/me/feed', args=None, post_args=args, method='POST')

    print status


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    # print resp
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
            # print "received page access token",page_access_token
            #frappe.db.set_value("Mobile Settings", None, "page_access_token", page_access_token)
    graph = facebook.GraphAPI(page_access_token)
    return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3