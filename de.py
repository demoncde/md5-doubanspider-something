import requests
import lxml
import time

def writeSet():
    with open('idSet.txt', 'w') as f:
        for item in idSet:
            f.write("%s\n" % item)
def loadSet():
    return set(line.strip() for line in open('idSet.txt'))
cookies = {
    "bid":"krcnFrbL9dw",
    "douban-fav-remind":"1",
    "__gads":"ID=851f9d3bc3f7e01f:T=1574288062:S=ALNI_MZHUww8i58N2tk8bFxbD_Xp9zOYkA",
    "ll":"\"118123\"",
    "__yadk_uid":"9VmZTFStieakW9L7nf0AXH0FOtxCnLc0",
    "_vwo_uuid_v2":"D9D09EBB03960548BBD50C7DC9E34823E|ae3bc3b5e57f2bef36baaa95e88fe5e6",
    "push_doumail_num":"0",
    "__utmv":"30149280.5695",
    "douban-profile-remind":"1",
    "__utmz":"30149280.1599142153.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "__utmc":"30149280",
    "ck":"VxIE",
    "ap_v":"0,6.0",
    "push_noty_num":"1",
    "_pk_ref.100001.8cb4":"%5B%22%22%2C%22%22%2C1601911139%2C%22https%3A%2F%2Fsite.douban.com%2F150757%2Froom%2F1603912%2F%22%5D",
    "_pk_ses.100001.8cb4":"*",
    "__utma":"30149280.983759122.1574288063.1601907534.1601911141.10",
    "__utmt":"1",
    "__utmb":"30149280.1.10.1601911141",
    "_pk_id.100001.8cb4":"3071abd5f9eac3cd.1574288062.9.1601911143.1601908387.",
    "dbcl2":"\"56952656:9vCTEApXqf4\""
}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
url = 'https://www.douban.com'
main_url = 'https://www.douban.com/people/56952656/'
group_url = "https://www.douban.com/group/567016/"
send_url = "https://www.douban.com/doumail/write"
mid_payload = {
    'to':'203703406'
}
payload = {
'ck': 'VxIE',
'to': '223947070',
'm_text': '如果想找英文Kindle电子书，可以去 www.kindle-book.cn 这个网站看一下，支持搜索，也支持自定书单，挺专业的。',
'm_submit': '好了，寄出去'
}
def generatePayload(userId):
    payload = {}
    payload['ck'] = "VxIE"
    payload['to'] = userId
    payload['m_text'] = '如果想找英文Kindle电子书，可以去 www.kindle-book.cn 这个网站看一下，支持搜索，也支持自定书单，挺专业的。'
    payload['m_submit'] = '好了，寄出去'
    return payload
'''
requests for group,find the valueable imformation.
'''
# group_info = requests.get(group_url, headers=headers, cookies = cookies)
'''
simulate human operation
'''
# r = requests.get(send_url, headers=headers, cookies = cookies, params= mid_payload)

'''
send user mail
'''
# r = requests.post(send_url, headers = headers, cookies = cookies, data=payload)

# html_text= group_info.content
html_doc = """
<!DOCTYPE html>
<html lang="zh-CN" class="ua-mac ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        kindle电子书资源小组
</title>
    
    
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/group/567016/">
    
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    


    <script >var _head_start = new Date();</script>
    <script src="https://img3.doubanio.com/f/shire/72ced6df41d4d158420cebdd254f9562942464e3/js/jquery.min.js"></script>
    <script src="https://img3.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js"></script>
    <link href="https://img3.doubanio.com/f/shire/859dba5cddc7ed1435808cf5a8ddde5792cd6e0c/css/douban.css" rel="stylesheet" type="text/css">
    <style type="text/css">
    
        a:link { color: #259; }
        a:visited { color: #769; }
        a:hover { color: #fff; }
        a:active { color: #fff; }
        


    </style>
    
    <script src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
    <link href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>

    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/6af93213c030bb33.css">
    <script></script>

    <link rel="stylesheet" href="https://img3.doubanio.com/f/group/2f4c6f83940e2bbb76f5a23a7d987b9093919799/css/group/init.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    
    <script type="text/javascript">var _body_start = new Date();</script>
    
   



    <link href="//img3.doubanio.com/dae/accounts/resources/19870c3/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <ul>
    <li>
    <a id="top-nav-doumail-link" href="https://www.douban.com/doumail/">豆邮</a>
    </li>
    <li class="nav-user-account">
      <a target="_blank" href="https://accounts.douban.com/passport/setting/" class="bn-more">
        <span>马克 塞诺斯的帐号</span><span class="arrow"></span>
      </a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://www.douban.com/mine/">个人主页</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/orders/">我的订单</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/wallet/">我的钱包</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://accounts.douban.com/passport/setting/">帐号管理</a>
              </td>
            </tr>
            <tr>
              <td>
                <a href="https://www.douban.com/accounts/logout?source=group&ck=VxIE">退出</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  <div class="top-nav-reminder">
    <a href="https://www.douban.com/notification/" class="lnk-remind">提醒</a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
        <p>加载中...</p>
      </div>
    </div>
  </div>

    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;56952656&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;56952656&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;56952656&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;56952656&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;56952656&quot;}">同城</a>
    </li>
    <li class="on">
      <a href="https://www.douban.com/group"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;56952656&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;56952656&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;56952656&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;56952656&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;56952656&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    USER_ID: "56952656",
    UPLOAD_AUTH_TOKEN: "56952656:9a9027f0ad610cf12ccf98666c13d91a660da94b",
    SSE_TOKEN: "c530cb828252f54863d7f7d47044f28417559da9",
    SSE_TIMESTAMP: "1601961561",
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/19870c3/shire/bundle.js" defer="defer"></script>




      
    









<div id="db-nav-group" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary clearfix">
    <div class="nav-logo">
      <a href="https://www.douban.com/group/">豆瓣小组</a>
    </div>

    <div class="nav-items">
    <ul>
        
        <li class="nav-item-first"><a href="https://www.douban.com/group/">我的小组</a></li>
      <li><a href="https://www.douban.com/group/explore">精选</a></li>
      <li><a href="https://www.douban.com/group/explore/culture">文化</a></li>
      <li><a href="https://www.douban.com/group/explore/travel">行摄</a></li>
      <li><a href="https://www.douban.com/group/explore/ent">娱乐</a></li>
      <li><a href="https://www.douban.com/group/explore/fashion">时尚</a></li>
      <li><a href="https://www.douban.com/group/explore/life">生活</a></li>
      <li><a href="https://www.douban.com/group/explore/tech">科技</a></li>
   </ul>
   </div>

    <div class="nav-search">
      <form id='form' action="https://www.douban.com/group/search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          
          <input type="hidden" name="cat" value="1019" />
          <label for="inp-query">小组、话题</label>
          <div class="inp"><input id="inp-query" name="q" size="22" maxlength="60" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
        </fieldset>
      </form>
    </div>
  </div>
  </div>

</div>

<script>
Do(function(){
  var nav = $('#db-nav-group');
  var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");inp[0]&&"placeholder"in inp[0]?(label.hide(),inp.attr("placeholder",label.text())):(""!==inp.val()&&label.hide(),inp.parent().click(function(){inp.focus(),label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){""===$.trim(this.value)?label.show():label.hide()}).keydown(function(){label.hide()})),inp.parents("form").submit(function(){if(!$.trim(inp.val()).length)return!1}),nav.find(".lnk-more, .lnk-account").click(function(n){n.preventDefault();var i,e=$(this),t=e.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");t.data("init")||(i=e.offset(),t.css({"margin-left":i.left-$(window).width()/2-t.width()+e.width()+parseInt(e.css("padding-right"),10)+"px",left:"50%",top:i.top+e.height()+"px"}),t.data("init",1),t.hide(),$("body").click(function(n){var i=$(n.target);i.hasClass("lnk-more")||i.hasClass("lnk-account")||i.closest("#db-usr-setting").length||i.closest("#db-productions").length||t.hide()})),"none"===t.css("display")?($(".dropdown").hide(),t.show()):$(".dropdown").hide()});
});
</script>




    <div id="wrapper">
        

        
<div id="content">
    
    
    <div id="group-info" class="clearfix">
        <div class="group-desc">
            <img align="left" valign="top" class="pil groupicon" src="https://img3.doubanio.com/view/group/sqxs/public/f01565cbd488a01.webp" alt="kindle电子书资源"/>
            <h1>
        kindle电子书资源
</h1>
            &nbsp; &nbsp;
            <div class="group-misc">
                
                        我是这个小组的成员
                        &gt; <a style="margin-left:6px;" href="https://www.douban.com/group/567016/?action=quit&amp;ck=VxIE" class="j a_confirm_link " title="退出小组">退出小组</a>
            </div>
        </div>
    </div>


    <div class="grid-16-8 clearfix">
        
        
        <div class="article">
               
    


    






    





    






<div class="group-board">
    <p>
    创建于2015-06-15 &nbsp; &nbsp;
    
    组长：<a href="https://www.douban.com/people/64783834/">徐戈</a>
    </p>



    <div class="group-intro">
            本小组致力于为大家搜集免费的包括但不限于kindle电子书资源，爱智求真，以书会友。期待能够团结一批有意思的人做一些有意义的事，最终目标做一个互联网实验，打造一个纯公益书籍分享论坛。
<br/>    
<br/>   目前小组数据库有图书上百万册，基本能够做到有求必应，你要想的我们都能给你找来，就算找不了，花钱也要给你找来。
<br/>
<br/>kindle读书交流一群 202754988。后期群将实行邀请制，欢迎书友的到来，之后争取策划一些活动，让大家深入互动交流。
<br/>
    </div>

    <div class="group-tags">
        小组标签&nbsp;&nbsp;
            <a class="tag" href="https://www.douban.com/search?cat=1019&amp;q=kindle">kindle</a>
            <a class="tag" href="https://www.douban.com/search?cat=1019&amp;q=电子书">电子书</a>
            <a class="tag" href="https://www.douban.com/search?cat=1019&amp;q=求书">求书</a>
    </div>

    <div class="group-rec">
          




  <script>
    var rec_url = 'https://www.douban.com/share/recommend?'
  </script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/9238d0db7d5fc042186ec54ebc5b4e64653f5e46/js/dshare.js"></script>

<div class="rec-sec">
  <span class="rec">
    
    
      <a href="https://www.douban.com/share/recommend?sanity_key=_f89e2&amp;apikey=&amp;name=kindle%E7%94%B5%E5%AD%90%E4%B9%A6%E8%B5%84%E6%BA%90&amp;image=https%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup%2Fsqxs%2Fpublic%2Ff01565cbd488a01.jpg&amp;redir=https%3A%2F%2Fwww.douban.com%2Fgroup%2F567016%2F&amp;btn_text=%E6%8E%A8%E8%8D%90&amp;href=https%3A%2F%2Fwww.douban.com%2Fgroup%2F567016%2F&amp;type=&amp;properties=%7B%7D&amp;desc=++++%E6%9C%AC%E5%B0%8F%E7%BB%84%E8%87%B4%E5%8A%9B%E4%BA%8E%E4%B8%BA%E5%A4%A7%E5%AE%B6%E6%90%9C%E9%9B%86%E5%85%8D%E8%B4%B9%E7%9A%84%E5%8C%85%E6%8B%AC%E4%BD%86%E4%B8%8D%E9%99%90%E4%BA%8Ekindle%E7%94%B5%E5%AD%90%E4%B9%A6%E8%B5%84%E6%BA%90%EF%BC%8C%E7%88%B1%E6%99%BA..." share-id="567016"
        data-user_id="56952656"
        data-name="kindle电子书资源"
        data-type=""
        data-desc="    本小组致力于为大家搜集免费的包括但不限于kindle电子书资源，爱智..."
        data-href="https://www.douban.com/group/567016/"
        data-image="https://img3.doubanio.com/view/group/sqxs/public/f01565cbd488a01.webp"
        data-properties="{}"
        data-text=""
        data-redir="https://www.douban.com/static/dshare_proxy.html"
        data-apikey=""
        data-heading=""
        data-object_kind="1019"
        data-object_id="567016"
        data-target_type="rec"
        data-target_action="0"
        data-action_props="{&#34;group_title&#34;:&#34;kindle电子书资源&#34;,&#34;group_url&#34;:&#34;https:\/\/www.douban.com\/group\/567016\/&#34;}"
        data-btn_text="推荐"
        data-sanity_key="_f89e2"
        class="lnk-sharing lnk-douban-sharing">推荐</a>
  </span>
</div>

    </div>
    <a name="topics"></a>
</div>



    <div id="group-topics" class="mod">
    





<div id="group-new-topic-bar">
    <div class="bns">
        <a href="new_topic" class="bn-post1 js-verify-account "
           data-is-verified="True" data-verify-url="https://www.douban.com/accounts/phone/verify"><span><i>+</i>发言</span></a>
    </div>

    
    <div class="topic-tab">
      <a href="https://www.douban.com/group/567016/#topics" class=on>最近讨论</a>
      <i>/</i>
    <a href="https://www.douban.com/group/567016/?type=essence#topics" >最热讨论</a>
    </div>
</div>


    <div class="">
        







    <table class="olt">
        <tr class="th">
            <td>讨论</td>
            <td>作者</td><td class="r-count" nowrap="nowrap">回应</td><td align="right">最后回应</td>
        </tr>
            

            <tr class="">
                <td class="title">
                        <span class="pl">
                            <img alt="[置顶]" src="https://img3.doubanio.com/pics/stick.gif"/>
                        </span>&nbsp;
                    
                    <a href="https://www.douban.com/group/topic/81796643/" title="Kindle 电子书资源上哪去找？（不断更新）" class="">
                       Kindle 电子书资源上哪去找？（不断更新）
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/64783834/" class="">徐戈</a>
                </td>
                <td nowrap="nowrap" class="r-count ">17</td>
                <td nowrap="nowrap" class="time">08-05 14:58</td>
            </tr>

            <tr class="">
                <td class="title">
                        <span class="pl">
                            <img alt="[置顶]" src="https://img3.doubanio.com/pics/stick.gif"/>
                        </span>&nbsp;
                    
                    <a href="https://www.douban.com/group/topic/81850045/" title="送给 Kindle 新人的宝贵建议" class="">
                       送给 Kindle 新人的宝贵建议
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/64783834/" class="">徐戈</a>
                </td>
                <td nowrap="nowrap" class="r-count ">11</td>
                <td nowrap="nowrap" class="time">07-28 15:56</td>
            </tr>

            <tr class="">
                <td class="title">
                        <span class="pl">
                            <img alt="[置顶]" src="https://img3.doubanio.com/pics/stick.gif"/>
                        </span>&nbsp;
                    
                    <a href="https://www.douban.com/group/topic/81795439/" title="Kindle 电子书资源站点汇总" class="">
                       Kindle 电子书资源站点汇总
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/64783834/" class="">徐戈</a>
                </td>
                <td nowrap="nowrap" class="r-count ">6</td>
                <td nowrap="nowrap" class="time">06-02 19:47</td>
            </tr>

            

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/107411069/" title="我的几个平时找书的工具分享，90%可以找到" class="">
                       我的几个平时找书的工具分享，90%可以找到
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/61429911/" class="">yuntiandi0001</a>
                </td>
                <td nowrap="nowrap" class="r-count ">6</td>
                <td nowrap="nowrap" class="time">10-06 11:12</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/153676251/" title="3.真·免费帮找书，还有我找不到的书？（后半句划掉）" class="">
                       3.真·免费帮找书，还有我找不到的书？（后半句划掉）
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/89099051/" class="">wz6z6z6</a>
                </td>
                <td nowrap="nowrap" class="r-count ">92</td>
                <td nowrap="nowrap" class="time">10-05 20:25</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/196117243/" title="《东野圭吾作品集》共64册 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《东野圭吾作品集》共64册 azw3+mobi+epub+txt kin...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">10-04 22:39</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195953878/" title="《一个人就一个人》刘同 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《一个人就一个人》刘同 azw3+mobi+epub+txt kindl...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">10-03 11:03</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188767793/" title="万本 kindle图书下载查询手册" class="">
                       万本 kindle图书下载查询手册
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Crosky/" class="">抚摸狗头</a>
                </td>
                <td nowrap="nowrap" class="r-count ">44</td>
                <td nowrap="nowrap" class="time">10-03 09:07</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195786485/" title="《沉默的真相》原著小说《长夜难明》紫金陈 azw3+mobi+epub kindle电子书下载" class="">
                       《沉默的真相》原著小说《长夜难明》紫金陈 azw3+m...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">10-01 13:54</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195723478/" title="《米兰·昆德拉作品集》（全套）azw3+mobi+epub+txt kindle电子书下载" class="">
                       《米兰·昆德拉作品集》（全套）azw3+mobi+epub+tx...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-30 18:44</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195471245/" title="2万多本书，有需要找书的可以找我" class="">
                       2万多本书，有需要找书的可以找我
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/154296995/" class="">周</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">09-29 09:57</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195503869/" title="《盗墓笔记》南派三叔 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《盗墓笔记》南派三叔 azw3+mobi+epub+txt kindle...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-28 18:09</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195396181/" title="《雪中悍刀行（全20册）》烽火戏诸侯 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《雪中悍刀行（全20册）》烽火戏诸侯 azw3+mobi+ep...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-27 19:16</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195178958/" title="求张贵兴《群象》《伏虎》资源" class="">
                       求张贵兴《群象》《伏虎》资源
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/129160966/" class="">养鸭汉</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-25 23:55</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/195169244/" title="《呼吸》特德·姜 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《呼吸》特德·姜 azw3+mobi+epub+txt kindle电子...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-25 22:28</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194919404/" title="《长夜难明》紫金陈（沉默的真相 原著）azw3+mobi+epub+txt kindle电子书下载" class="">
                       《长夜难明》紫金陈（沉默的真相 原著）azw3+mobi+...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-23 22:33</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194789941/" title="从零开始学运营" class="">
                       从零开始学运营
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-22 22:44</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194750189/" title="《刑法学讲义》罗翔 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《刑法学讲义》罗翔 azw3+mobi+epub+txt kindle电...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-22 17:19</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194521642/" title="《强风吹拂》三浦紫苑 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《强风吹拂》三浦紫苑 azw3+mobi+epub+txt kindle...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-20 20:31</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194335423/" title="《正常人》萨莉·鲁尼 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《正常人》萨莉·鲁尼 azw3+mobi+epub+txt kindle...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-19 12:04</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194149087/" title="《第一炉香》张爱玲 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《第一炉香》张爱玲 azw3+mobi+epub+txt kindle电...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-17 21:28</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/194062458/" title="需要办理出版物经营许可证的  价格优惠 官网可查" class="">
                       需要办理出版物经营许可证的  价格优惠 官网可查
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/221734297/" class="">涛</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-17 10:04</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/139469467/" title="东野圭吾全套 91 部作品集 全格式 《白夜行》《解忧杂货店》" class="">
                       东野圭吾全套 91 部作品集 全格式 《白夜行》《解...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/192617185/" class="">九月云归</a>
                </td>
                <td nowrap="nowrap" class="r-count ">36</td>
                <td nowrap="nowrap" class="time">09-16 19:44</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193854966/" title="《价值》张磊 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《价值》张磊 azw3+mobi+epub+txt kindle电子书下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-15 16:27</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193697694/" title="《理想国译丛》（全套）azw3+mobi+epub+txt kindle电子书下载" class="">
                       《理想国译丛》（全套）azw3+mobi+epub+txt kindle...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/MissCoooooool/" class="">Co.Co.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-14 12:47</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193285409/" title="求 鲁迅文集 资源！谢谢🙏" class="">
                       求 鲁迅文集 资源！谢谢🙏
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/220516841/" class="">撒贝宁</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">09-13 23:12</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193606270/" title="《马伯庸精选作品集（共23册）》azw3+mobi+epub+txt kindle电子书下载" class="">
                       《马伯庸精选作品集（共23册）》azw3+mobi+epub+tx...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-13 17:09</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193419967/" title="《你当像鸟飞往你的山》塔拉·韦斯特弗 azw3+mobi+epub+txt kindle电子书下载" class="">
                       《你当像鸟飞往你的山》塔拉·韦斯特弗 azw3+mobi+...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-12 11:12</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190039965/" title="《一往无前：雷军亲述小米热血10年》azw3+mobi+epub+txt 电子书" class="">
                       《一往无前：雷军亲述小米热血10年》azw3+mobi+epu...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">09-12 09:38</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193155747/" title="电子书寻找" class="">
                       电子书寻找
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/153318728/" class="">梁小超</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-10 13:34</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/193152184/" title="《正常人》萨莉·鲁尼 azw3+mobi+epub+txt 电子书下载" class="">
                       《正常人》萨莉·鲁尼 azw3+mobi+epub+txt 电子书下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/KingKongbaby/" class="">KingKong.</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-10 13:07</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/192970281/" title="求书单里的电子书" class="">
                       求书单里的电子书
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/56405967/" class="">reality</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-09 09:00</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190175713/" title="《半泽直树（全4册）》池井户润 azw3+mobi+epub+txt 电子书" class="">
                       《半泽直树（全4册）》池井户润 azw3+mobi+epub+tx...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">09-07 16:26</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/192201469/" title="《82年生的金智英》赵南柱 azw3+mobi+epub+txt 电子书下载" class="">
                       《82年生的金智英》赵南柱 azw3+mobi+epub+txt 电...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-03 16:15</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/192085546/" title="《杨小凯学术文库》azw3+mobi+epub+txt 电子书 下载" class="">
                       《杨小凯学术文库》azw3+mobi+epub+txt 电子书 下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-02 19:24</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/191936401/" title="我在当当网买书的一个教训" class="">
                       我在当当网买书的一个教训
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/197881998/" class="">豆友197881998</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">09-01 17:41</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/191393938/" title="求盐的代价资源" class="">
                       求盐的代价资源
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/191182058/" class="">yhy</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-28 19:59</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/191263812/" title="环球科学2020年8月高清" class="">
                       环球科学2020年8月高清
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/222051942/" class="">杂志惠</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-27 22:48</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190765986/" title="《旋涡》《漩涡》伊藤润二 azw3+mobi+epub+txt 电子书 漫画 下载" class="">
                       《旋涡》《漩涡》伊藤润二 azw3+mobi+epub+txt 电...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-24 15:33</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190506650/" title="《晚熟的人》莫言 新书 azw3+mobi+epub+PDF+txt 电子书" class="">
                       《晚熟的人》莫言 新书 azw3+mobi+epub+PDF+txt 电...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-22 19:37</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188984194/" title="电子书分享" class="">
                       电子书分享
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">08-22 08:17</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190317241/" title="《两京十五日》马伯庸 azw3+mobi+epub+txt 电子书" class="">
                       《两京十五日》马伯庸 azw3+mobi+epub+txt 电子书
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-21 14:47</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190220973/" title="《哈利·波特（共7部）》J.K.罗琳 azw3+mobi+epub+txt 电子书" class="">
                       《哈利·波特（共7部）》J.K.罗琳 azw3+mobi+epub+...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/Downey_H/" class="">Dominic_H</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-20 21:56</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190120068/" title="睡个好觉[pdf,mobi,epub,txt]" class="">
                       睡个好觉[pdf,mobi,epub,txt]
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-20 10:25</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/190017355/" title="钱从哪里来[pdf,mobi,epub,txt]" class="">
                       钱从哪里来[pdf,mobi,epub,txt]
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-19 15:38</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189880705/" title="那些比答案更重要的好问题-epub、mobi、awz3下载" class="">
                       那些比答案更重要的好问题-epub、mobi、awz3下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count ">1</td>
                <td nowrap="nowrap" class="time">08-18 23:39</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189856236/" title="《那些忧伤的年轻人》[pdf,mobi,epub,txt]" class="">
                       《那些忧伤的年轻人》[pdf,mobi,epub,txt]
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-18 14:12</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189620963/" title="假性亲密关系[pdf,mobi,epub,txt]" class="">
                       假性亲密关系[pdf,mobi,epub,txt]
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/159361983/" class="">追星星的你</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-16 22:42</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189499073/" title="书籍，摄影集，电影，插画资源付费 会员免费🆓" class="">
                       书籍，摄影集，电影，插画资源付费 会员免费🆓
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/75953877/" class="">立往生</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-16 09:03</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189084544/" title="《长安客》-kindle版下载" class="">
                       《长安客》-kindle版下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-13 15:52</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/189083638/" title="银河系边缘的小失常 【埃特加·凯雷特】-epub、mobi、azw3电子书下载" class="">
                       银河系边缘的小失常 【埃特加·凯雷特】-epub、mob...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-13 15:46</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188979049/" title="圆圈正义【罗翔】-txt、epub、mobi、azw3电子书资源下载" class="">
                       圆圈正义【罗翔】-txt、epub、mobi、azw3电子书资...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-12 21:22</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188895949/" title="这个社会会好吗-epub、mobi、awz3下载
" class="">
                       这个社会会好吗-epub、mobi、awz3下载

                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-12 11:30</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188826193/" title="坏小孩-epub、mobi、azw3电子资源下载" class="">
                       坏小孩-epub、mobi、azw3电子资源下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-11 21:13</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188825977/" title="马伯庸作品合集-epub+mobi+azw3下载
" class="">
                       马伯庸作品合集-epub+mobi+azw3下载

                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-11 21:12</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188798066/" title="刑法学讲义-EPUB电子资源下载" class="">
                       刑法学讲义-EPUB电子资源下载
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-11 17:46</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188740199/" title="冰菓/古典部系列合集（米泽穗信）-epub、mobi、azw3电子资源下载" class="">
                       冰菓/古典部系列合集（米泽穗信）-epub、mobi、azw...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-11 11:27</td>
            </tr>

            <tr class="">
                <td class="title">
                    
                    <a href="https://www.douban.com/group/topic/188619522/" title="镖人漫画系列合集（1-9） -epub、mobi、azw3电子资源下载	
" class="">
                       镖人漫画系列合集（1-9） -epub、mobi、azw3电子资...
                    </a>
                </td>
                <td nowrap="nowrap">
                    <a href="https://www.douban.com/people/84813476/" class="">栗子的精神食粮</a>
                </td>
                <td nowrap="nowrap" class="r-count "></td>
                <td nowrap="nowrap" class="time">08-10 15:22</td>
            </tr>

    </table>







    </div>

        <div class="group-topics-more">
            &gt; <a href="https://www.douban.com/group/567016/discussion?start=50">更多小组讨论</a>
        </div>
        






<div class="group-topic-search">
    <form action="/group/search" method="get">
        <input type="hidden" value="567016" name="group"/>
        <input type="hidden" value="1013" name="cat"/>
        <div class="inp">
        <input type="text" value="" maxlength="60" size="22" title="搜索本组讨论" name="q" class="j a_search_text "/>
        </div>
        <div class="inp-btn">
          <input type="submit" value="搜索"/>
        </div>
    </form>
</div>


   </div>


        </div>
        <div class="aside">
                
    











    
<div class="mod">

        
    
    
    <h2>
        最近加入
            
    </h2>

    
<style>
  .member-list ul {
    margin-top: -20px;
    letter-spacing: -0.31em;
    *letter-spacing: normal;
    word-spacing: -0.43em;
    font-size: 0;
  }
  .member-list .pic {
    overflow: hidden;
    margin-bottom: 5px;
  }
  .member-list li {
    display: inline-block;
    *display: inline;
    zoom: 1;
    width: 75px;
    margin-top: 20px;
    text-align: center;
    font-size: 12px;
    vertical-align: top;
    letter-spacing: normal;
    word-spacing: normal;
  }
  .member-list .name {
    clear: both;
  }
  .u_actions { display:inline-block;*display:inline;zoom:1;vertical-align:middle; }
</style>
<div class="member-list">
<ul>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/163777979/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u163777979-11.jpg" class="imgnoga" alt="Ann"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/163777979/" class="">Ann</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/223947070/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u223947070-1.jpg" class="imgnoga" alt="就想看本书"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/223947070/" class="">就想看本书</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/203703406/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u203703406-1.jpg" class="imgnoga" alt="向阳"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/203703406/" class="">向阳</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/200403985/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u200403985-1.jpg" class="imgnoga" alt="哈密瓜"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/200403985/" class="">哈密瓜</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/196063851/" class="nbg">
            <img src="https://img9.doubanio.com/icon/u196063851-5.jpg" class="imgnoga" alt="🍰🧨🪓"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/196063851/" class="">🍰🧨🪓</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/168854227/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u168854227-1.jpg" class="imgnoga" alt="大军"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/168854227/" class="">大军</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/189750814/" class="nbg">
            <img src="https://img9.doubanio.com/icon/u189750814-4.jpg" class="imgnoga" alt="白日梦大圣"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/189750814/" class="">白日梦大圣</a>
        </div>
    </li>
    
    <li class="">
        <div class="pic">
        <a href="https://www.douban.com/people/137938469/" class="nbg">
            <img src="https://img3.doubanio.com/icon/u137938469-1.jpg" class="imgnoga" alt="复古御风者"/>
        </a>
        </div>

        <div class="name">
            <a href="https://www.douban.com/people/137938469/" class="">复古御风者</a>
        </div>
    </li>
</ul>
</div>


</div>


    



    







    <div class="mod side-nav">
    
        <p>&gt; <a href="https://www.douban.com/group/567016/members">浏览所有成员 (2770)</a>

                <p>&gt; <a href="https://www.douban.com/group/567016/invite">邀请好友</a><br>

    




    </div>

    <div id="dale_group_home_middle_right"></div>
    <div id="dale_group_home_middle_right_large"></div>
    <div id="dale_group_home_middle_right2"></div>


        





    
    <div class="mod">
        
    <h2>
        这个小组的成员也喜欢去
            
    </h2>

        <div class="bd">
            






<div class="group-list">
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/366504/"><img src="https://img9.doubanio.com/icon/user.jpg" class="m_sub_img" alt="Kindle资源共享"/></a></div>
    <div class="title"><a  title="Kindle资源共享" href="https://www.douban.com/group/366504/" class="">Kindle资源共享</a> <span>(813)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/590106/"><img src="https://img9.doubanio.com/view/group/sqxs/public/6858c1a2ed71954.webp" class="m_sub_img" alt="kindle电子书资源分享"/></a></div>
    <div class="title"><a  title="kindle电子书资源分享" href="https://www.douban.com/group/590106/" class="">kindle电子书资源分享</a> <span>(375)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/504198/"><img src="https://img3.doubanio.com/view/group/sqxs/public/0e6e100c0a38f81.webp" class="m_sub_img" alt="kindle电子书分享"/></a></div>
    <div class="title"><a  title="kindle电子书分享" href="https://www.douban.com/group/504198/" class="">kindle电子书分享</a> <span>(1489)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/476827/"><img src="https://img1.doubanio.com/view/group/sqxs/public/38692eb75812a4a.webp" class="m_sub_img" alt="Kindle电子书 : 爱读书 爱分享"/></a></div>
    <div class="title"><a  title="Kindle电子书 : 爱读书 爱分享" href="https://www.douban.com/group/476827/" class="">Kindle电子书 : 爱读书...</a> <span>(2549)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/526738/"><img src="https://img1.doubanio.com/view/group/sqxs/public/bba976ac4c4941b.webp" class="m_sub_img" alt="kindle书库"/></a></div>
    <div class="title"><a  title="kindle书库" href="https://www.douban.com/group/526738/" class="">kindle书库</a> <span>(276)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/486022/"><img src="https://img3.doubanio.com/view/group/sqxs/public/cb9b70ee3d02b4e.webp" class="m_sub_img" alt="Kindle 书屋"/></a></div>
    <div class="title"><a  title="Kindle 书屋" href="https://www.douban.com/group/486022/" class="">Kindle 书屋</a> <span>(176)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/309262/"><img src="https://img9.doubanio.com/icon/user.jpg" class="m_sub_img" alt="Kindle 电子书 分享"/></a></div>
    <div class="title"><a  title="Kindle 电子书 分享" href="https://www.douban.com/group/309262/" class="">Kindle 电子书 分享</a> <span>(31810)</span>
    </div>
    </div>
    
    <div class="group-list-item">
        <div class="pic"><a  href="https://www.douban.com/group/498253/"><img src="https://img3.doubanio.com/view/group/sqxs/public/5baefbddc54fb8d.webp" class="m_sub_img" alt="Kindle阅读人生"/></a></div>
    <div class="title"><a  title="Kindle阅读人生" href="https://www.douban.com/group/498253/" class="">Kindle阅读人生</a> <span>(115)</span>
    </div>
    </div>
</div>









        </div>
    </div>





    <!--- douban ad begin -->
    <div id="dale_each_group_home_bottom_right"></div>
    <!--- douban ad end -->

        </div>
        <div class="extra">
            
        </div>
    </div>
</div>

        
<div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2020 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/group" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

</div>

    </div>
    
    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/237b940e45c3bc33.js"></script>
    
    <!--- douban ad begin -->
        
        




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '56952656',
            browserId = 'krcnFrbL9dw',
            criteria = '1:567016|2:kindle|2:电子书|2:求书|3:/group/567016/',
            preview = '',
            debug = false,
            adSlots = ['dale_group_home_middle_right', 'dale_group_home_middle_right2', 'dale_group_home_middle_right_large', 'dale_group_home_left_bottom', 'dale_each_group_home_bottom_right'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/ZGJhYzhmaC9mL2FkanMvOTY0ZDI5MjQ5N2ViOGI2ZGU3ODdkYmI3YTk3NDliMTJlMzNmMGNlYy9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










    <!--- douban ad end -->
    <script src="https://img3.doubanio.com/f/group/7256e892ef5a810202e0726f69f1662f878c5302/js/group/index.js"></script>

    
    








<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_setCampNameKey', 'dcn']);
_gaq.push(['_setCampSourceKey', 'dcs']);
_gaq.push(['_setCampMediumKey', 'dcm']);
_gaq.push(['_setCampTermKey', 'dct']);
_gaq.push(['_setCampContentKey', 'dcc']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);

    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]);
    
    _gaq.push(['_setCustomVar', 2, 'group', 'kindle电子书资源', 3])
    _gaq.push(['_setCustomVar', 3, 'tags', 'kindle|电子书|求书|', 3])
_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);
        _gaq.push(['_trackEvent', 'group tag', 'view', 'kindle', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '电子书', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '求书', 0, true]);
    _gaq.push(['_setVar', '5695']);
window._ga_init = function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
};
if (window.addEventListener) {
    window.addEventListener('load', _ga_init, false);
} else {
    window.attachEvent('onload', _ga_init);
}
</script>






    <!-- dae-web-group--default-798cc7b595-65xlv-->


  <script>_SPLITTEST=''</script>
</body>

</html>



"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
subContent = soup.find("div",class_ = "member-list")
import re
regex = r"\d+"
idSet = set(('163777979','223947070'))
idDict = {}
for link in subContent.find_all('div',class_="name"):
    userIdRaw = link.a.get('href')
    userName = link.a.string
    userId = re.search(regex,userIdRaw).group(0)
    # print(userId)
    # print(re.findall(regex,userId))
    if userId not in idSet:
        idSet.add(userId)
        idDict[userName] = userId
        payloadfuc = generatePayload(userId)
        # print(payloadfuc)

        sendMailRequest = requests.post(send_url, headers=headers, cookies=cookies, data=payloadfuc)
        # time.sleep(5)
# print(subContent)
# print(idSet)
print(idDict)
