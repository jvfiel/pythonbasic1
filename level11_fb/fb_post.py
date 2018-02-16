from level11_fb.fb_api import post_feed

def test_post():
    #sample_photo = frappe.get_site_path() + '/public' + frappe.db.get_value("Mobile Settings", None, "test_fb_photo")
    sample_photo = '/home/jvfiel/projects/pythonlegends/level11_fb/owl.jpg'
    img_list = [sample_photo]
    #msg = frappe.db.get_value("Mobile Settings", None, "test_fb_message_post")
    msg = "Hello World"
    post_feed(msg,img_list)

test_post()