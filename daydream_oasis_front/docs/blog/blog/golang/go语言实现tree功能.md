
<BlogInfo title="go语言实现tree功能" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=26 category="golang" tag_list="[]" create_time="2022.10.12 16:39:25.491062" update_time="2023.04.06 22:32:06.634953" />

^^^^^^^^^
<p>最近在学go语言，刚好学到了文件操作这一块，上班摸鱼间隙实现了一个类似于tree的功能。</p>
<pre data-widget="codeSnippet">
<code class="hljs language-Go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
	<span class="hljs-string">&#34;fmt&#34;</span>
	<span class="hljs-string">&#34;os&#34;</span>
)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">dir_r</span><span class="hljs-params">(dir <span class="hljs-type">string</span>, n <span class="hljs-type">int</span>)</span></span> {
	f, err := os.Open(dir)
	<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> {
		fmt.Printf(<span class="hljs-string">&#34;err: %v
&#34;</span>, err)
		<span class="hljs-keyword">return</span>
	}
	fi, err2 := f.Readdir(<span class="hljs-number">0</span>)
	<span class="hljs-keyword">if</span> err2 != <span class="hljs-literal">nil</span> {
		fmt.Printf(<span class="hljs-string">&#34;err2: %v
&#34;</span>, err2)
		<span class="hljs-keyword">return</span>
	}
	<span class="hljs-keyword">for</span> _, f_obj := <span class="hljs-keyword">range</span> fi {

		<span class="hljs-keyword">for</span> i := <span class="hljs-number">0</span>; i &lt; n; i++ {
			<span class="hljs-built_in">print</span>(<span class="hljs-string">&#34;    &#34;</span>)
		}
		<span class="hljs-built_in">print</span>(<span class="hljs-string">&#34;└──&#34;</span>)
		fmt.Println(f_obj.Name())
		<span class="hljs-keyword">if</span> f_obj.IsDir() {
			<span class="hljs-comment">// n += 1</span>
			dir_r(dir+<span class="hljs-string">&#34;/&#34;</span>+f_obj.Name(), n+<span class="hljs-number">1</span>)
		}
	}

}

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> {

	dir_r(<span class="hljs-string">&#34;.&#34;</span>, <span class="hljs-number">0</span>)

}
</code>
</pre>
<p>效果如下，还算不错：</p>
<p><img src="../../../media/image/2023/04/06/image.cc6edb2ad48711edb70fcd63b0e7ad35.png" alt="image.cc6edb2ad48711edb70fcd63b0e7ad35.png" /></p>

