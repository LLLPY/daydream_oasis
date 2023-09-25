
<BlogInfo title="Django中ckeditor的使用" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=170 category="Django" tag_list="['Django', '插件', 'ckeditor']" create_time="2022.01.17 21:39:20.760395" update_time="2022.07.11 10:58:39" />

^^^^^^^^^
<p><span style="font-size:18px"><a href="https://baike.baidu.com/item/CKEditor/626256?fr=aladdin">CKEditor即大名鼎鼎的FCKeditor（文本编辑器），它终于在最近发布新版本了，与增加版本号不同，这次完全把它改名了，更名为CKeditor。这应该是和它的开发公司CKSource(波兰华沙的公司)的名字有关吧，该公司的另一个产品为CKFinder（一个Ajax文件管理器），这次可能为了保持一致，将FCK更改为CK，但是版本号继承了下来，为CKeditor3.0版。</a></span></p>

<p><span style="font-size:18px">有支持django的第三方插件<a href="https://pypi.org/project/django-ckeditor/">django-ckeditor</a></span></p>

<p><span style="font-size:18px">我感觉对于博客系统这种内容型的网站来说，这个编辑器还是非常nice的~</span></p>

<p><span style="font-size:18px">先看一下效果图：</span></p>

<p><img src="../media/image/2022/02/02/image-20220202212857-1.png" style="height:445px; width:900px" /></p>

<p><span style="font-size:18px">这个是我今天基本上花费了一整天才配置好的，在配置过程中还是踩了非常多的坑的</span><span style="font-size:18px">，所以想写下这篇博客来记录我今天踩的坑，不过最后终于配置好还是比较欣慰的，打不倒我的只会使我更加强大嘿嘿</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">还是一步一步来：</span></p>

<p><span style="font-size:18px">1.安装：pip install django-ckeditor</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">2.添加到installed_app</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">可以看到我添加了两个：</span></p>

<pre>
<strong><span style="color:#e74c3c"><span style="font-size:18px">&#39;ckeditor&#39;,  
&#39;ckeditor_uploader&#39;, #富文本中图片的上传</span></span></strong></pre>

<p><span style="font-size:18px">如果不需要在编辑器中上传图片，只需要添加第一个即可！但是它既然都提供了上传图片这个功能，何必不用呢？也正是这个上传图片的功能让我倒腾了半天！</span></p>

<p><br />
<span style="font-size:18px">3.定义form（这里使用的是可以上传图片的）</span></p>

<pre>
<span style="font-size:16px">from django import forms
from ckeditor_uploader.widgets import <span style="color:#e74c3c">CKEditorUploadingWidget</span>
from app.models import Blog
class BlogForm(forms.ModelForm):

    content=forms.CharField(widget=<span style="background-color:#e74c3c">CKEditorUploadingWidget</span>(
        attrs={&#39;class&#39;: &#39;ckeditor&#39;, &#39;name&#39;: &#39;content&#39;}
    ),label=&#39;&#39;,required=True,)

    class Meta:
        model=Blog
        fields=[&#39;content&#39;]
      </span></pre>

<p><span style="font-size:18px">4.配置url</span></p>

<p><img src="../media/image/2022/02/02/image-20220202213052-2.png" style="height:402px; width:1264px" /></p>

<pre>
<span style="font-size:18px"><span style="background-color:#e74c3c">+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)这个千万不能漏掉，不然会上传文件失败！</span></span></pre>

<p><span style="font-size:18px">5.在settings中配置图片的上传路径</span></p>

<p><img src="../media/image/2022/02/02/image-20220202213130-3.png" style="height:146px; width:1048px" /></p>

<p><span style="font-size:18px">按照如上配置后，上传的图片会自动保存在项目根目录下的media目录中。</span></p>

<p><span style="font-size:18px">6.在admin中指定form</span></p>

<p><img src="../media/image/2022/02/02/image-20220202213350-4.png" style="height:280px; width:727px" /></p>

<p><span style="font-size:18px">完成这到这步后，admin管理台上就可以正常显示富文本编辑器了！</span></p>

<p><img src="../media/image/2022/02/02/image-20220202213515-5.png" style="height:648px; width:900px" /></p>

<p><span style="font-size:18px">admin控制台使用ckeditor的配置就完成了！这个相对来说还是比较简单的，但是对于一个博客系统来说，管理台一般只有管理员才能进行查看和编辑，如果普通的用户也需要编辑自己的博客，就需要另外编写一个页面！</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">定义一个一般用户能使用的富文本编辑器，并且能上传图片。</span></p>

<p><span style="font-size:18px">上面的步骤还是不变的。</span></p>

<p><span style="font-size:18px">按照正常的思路来，我只需要只需要使用模板语言将form嵌套在html中并且加上safe修饰词渲染成html就行了,所以正常步骤如下：</span></p>

<p><img src="../media/image/2022/02/02/image-20220202213736-6.png" style="height:379px; width:807px" /></p>

<p><span style="font-size:18px">定义好模板后，使用locals读取上文出现的所有变量，方便到模板中直接引用。但是，现实总是和想法不一样，错误显示的图我就不截了。这里需要在需在html文件中额外引入ckeditor.js文件即可：</span></p>

<p><img src="../media/image/2022/02/02/image-20220202214037-7.png" style="height:505px; width:1243px" /></p>

<p><span style="font-size:18px">引入这个js文件后就可以正常显示了！</span></p>

<p><span style="font-size:18px">但是！但是！但是！就算这里form中使用的是CKEditorUploadingWidget，这里生成出来的编辑器中任然是无法上传图片的！！！所以只好问度娘了。。。</span></p>

<p><span style="font-size:18px">试了网上的n种方法后，终于找到了一个可行的方法！！（这其中的辛酸不说了。。。）</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">方法就是找打插件库中的config.js文件，在其中添加一个配置：config.filebrowserImageUploadUrl= &quot;/ckeditor/upload/&amp;responseType=json&quot;;</span></p>

<p><span style="font-size:18px">顾名思义这个就是配置图片的上传路径，我这里的图片的上传路径为：/ckeditor/upload/&amp;responseType=json，其中ckeditor为你自己添加url时取的名字，其他的默认就行，&amp;responseType=json这个属性千万不能掉，否则也会失败！</span></p>

<p><span style="font-size:18px">完成以上的配置后，我刷新页面，再次点击图片那个按钮时，它出现了！不错，上传图片的选项它出现了！！！流出来激动的泪水。。。</span></p>

<p><span style="font-size:18px">但是！但是！你以为这就完了！这个在本地的图片上传功能确实完成了！</span></p>

<p><span style="font-size:18px">当我把项目重新上传到服务器，收集静态文件，关闭项目，启动项目，这熟练的手法我就不说了，当我激动的点开编辑页面时，我人又傻了！不仅没有图片上传的按钮！就连富文本的框框都没了！！？？？打开控制台，果不其然有报错！</span></p>

<p><span style="font-size:18px">报错内容：Refused to execute script from &#39;xxxx&#39; because its MIME type (&#39;text/html&#39;) is not executable, and strict MIME type checking is enabled.</span></p>

<p><span style="font-size:18px">我能有啥办法呢，再次去找度娘！</span></p>

<p><span style="font-size:18px">一顿操作后，没看到一个解决的方法。。。</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">根据我个人的推断，应该就是这个文件加载失败，但是反复查看文件的加载路径，没错呀！？按照正常来说，在注册的app中添加了ckeditor这个库后，在使用collectstatic命令时，django是会去收集该包下的static。可是这里的情况是没有收集到。。。</span></p>

<p><span style="font-size:18px">我还能有啥办法呢，暴力一点吧，直接把ckeditor的static中的所有内容拷贝到我自己的static中喽</span></p>

<p><img src="../media/image/2022/02/02/image-20220202214213-8.png" style="height:312px; width:321px" /></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">最后，再次上传项目，重启项目，终于看到了那个富文本编辑框！</span></p>

<p><span style="font-size:18px">哎，这一天没有白费~&nbsp;</span></p>

<p><span style="font-size:18px">每天进步一点点嘿嘿~</span><img src="../media/image/2022/02/02/image-20220202214225-9.gif" style="height:48px; width:48px" /><img src="../media/image/2022/02/02/image-20220202214225-9.gif" style="height:48px; width:48px" /><img src="../media/image/2022/02/02/image-20220202214225-9.gif" style="height:48px; width:48px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><br />
&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

