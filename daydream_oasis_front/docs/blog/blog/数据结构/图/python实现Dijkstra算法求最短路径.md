
<BlogInfo title="python实现Dijkstra算法求最短路径" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=147 category="图" tag_list="['最短路径', '最小生成树', '图']" create_time="2022.06.04 19:50:17.814195" update_time="2022.06.04 19:50:17" />

^^^^^^^^^
<h1>前言</h1>

<p>最近在考研复习，刚好学到图这一章了，然后也是学到关于图最难的几个部分了，一个是最小生成树（Prim算法和Kruskal算法），还一个就是最短距离问题了（Dijkstra算法和Floyd算法），我感觉前三个算法都还蛮好理解，就是最后一个Floyd有点没整明白，前三个算法基本上都用到贪心的思想，Prim每次都选择当前未使用的消耗最小的顶点（选点）；Kruskal每次都是当前未使用的权值最小的边（选边）；Dijkstra的思想和Prim的思想大致一直。</p>

<p>这里我就直接贴出源码了，python实现的，有兴趣的可以运行试试（反正考研也不会考python代码<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/5fe82103dfcf4ecf8a3709f51b489691.jpeg" style="height:34px; width:34px" />）</p>

<p>Dijkstra算法求最短路径</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># -*- coding: UTF-8 -*-</span>
<span class="hljs-string">&#39;&#39;&#39;
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll_107Dijkstra算法求解最短路径.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/6/1 9:22             
   *****************************************
&#39;&#39;&#39;</span>


<span class="hljs-keyword">def</span> <span class="function_ hljs-title">dijkstra_min_distance</span>(<span class="hljs-params">start, target, graph</span>):
    <span class="hljs-keyword">if</span> start <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> graph[<span class="hljs-string">&#39;V&#39;</span>] <span class="hljs-keyword">or</span> target <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> graph[<span class="hljs-string">&#39;V&#39;</span>]: <span class="hljs-keyword">return</span> <span class="hljs-string">&#39;无效起点或终点！&#39;</span>

    visited = {}  <span class="hljs-comment"># 记录顶点的访问情况</span>
    dist = {}  <span class="hljs-comment"># 记录最短距离</span>
    path = [start]  <span class="hljs-comment"># 记录最短路径上的每一个顶点</span>
    V, E = graph[<span class="hljs-string">&#39;V&#39;</span>], graph[<span class="hljs-string">&#39;E&#39;</span>]
    <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> V:
        visited[node] = <span class="hljs-number">0</span>  <span class="hljs-comment"># 0表示没有访问 1表示已访问</span>
        dist[node] = -<span class="hljs-number">1</span>  <span class="hljs-comment"># -1表示无限远</span>
    dist[start] = <span class="hljs-number">0</span>  <span class="hljs-comment"># 到自己的距离为0</span>
    visited[start] = <span class="hljs-number">1</span>

    <span class="hljs-comment"># 初始化到各顶点的距离</span>
    <span class="hljs-keyword">for</span> e <span class="hljs-keyword">in</span> E:
        <span class="hljs-keyword">if</span> e[<span class="hljs-number">0</span>] == start:
            dist[e[<span class="hljs-number">1</span>]] = E[e]

    <span class="hljs-comment"># while not all(visited.values()):  # 直到访问完所有顶点 求到所有顶点的最短距离</span>
    <span class="hljs-keyword">while</span> <span class="hljs-keyword">not</span> visited[target]:  <span class="hljs-comment"># 仅求到终点的距离</span>
        <span class="hljs-comment"># 在所有可达的但未访问的顶点中，寻找距离最近的一个</span>
        cur_E_li = [(e, E[e]) <span class="hljs-keyword">for</span> e <span class="hljs-keyword">in</span> E <span class="hljs-keyword">if</span> visited[e[<span class="hljs-number">0</span>]] <span class="hljs-keyword">and</span> <span class="hljs-keyword">not</span> visited[e[<span class="hljs-number">1</span>]]]  <span class="hljs-comment"># 所有可达但未访问的顶点</span>
        cur_E_li.sort(key=<span class="hljs-keyword">lambda</span> a: a[<span class="hljs-number">1</span>])  <span class="hljs-comment"># 按照距离进行排序</span>
        <span class="hljs-built_in">print</span>(cur_E_li)
        min_edge_w = cur_E_li[<span class="hljs-number">0</span>]  <span class="hljs-comment"># 第一个就是距离最短的那一个</span>
        new_start_node = min_edge_w[<span class="hljs-number">0</span>][<span class="hljs-number">1</span>]

        <span class="hljs-comment"># 刷新最短距离</span>
        <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> dist:
            new_edge = (new_start_node, node)
            <span class="hljs-keyword">if</span> new_edge <span class="hljs-keyword">in</span> E:
                <span class="hljs-keyword">if</span> dist[node] == -<span class="hljs-number">1</span>:
                    dist[node] = dist[new_start_node] + E[new_edge]
                <span class="hljs-keyword">else</span>:
                    dist[node] = <span class="hljs-built_in">min</span>(dist[node], dist[new_start_node] + E[new_edge])

        <span class="hljs-comment"># 更新visited</span>
        visited[new_start_node] = <span class="hljs-number">1</span>
        path.append(new_start_node)  <span class="hljs-comment"># 将当前节点更新到最短路径上</span>

    <span class="hljs-keyword">return</span> path, dist[target]


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    V = {<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>}  <span class="hljs-comment"># 顶点集</span>

    E = {  <span class="hljs-comment"># 边集</span>
        (<span class="hljs-number">1</span>, <span class="hljs-number">2</span>): <span class="hljs-number">10</span>,  <span class="hljs-comment"># (起点,终点):权值</span>
        (<span class="hljs-number">1</span>, <span class="hljs-number">5</span>): <span class="hljs-number">5</span>,
        (<span class="hljs-number">2</span>, <span class="hljs-number">3</span>): <span class="hljs-number">1</span>,
        (<span class="hljs-number">2</span>, <span class="hljs-number">5</span>): <span class="hljs-number">2</span>,
        (<span class="hljs-number">3</span>, <span class="hljs-number">4</span>): <span class="hljs-number">4</span>,
        (<span class="hljs-number">4</span>, <span class="hljs-number">1</span>): <span class="hljs-number">7</span>,
        (<span class="hljs-number">4</span>, <span class="hljs-number">3</span>): <span class="hljs-number">6</span>,
        (<span class="hljs-number">5</span>, <span class="hljs-number">2</span>): <span class="hljs-number">3</span>,
        (<span class="hljs-number">5</span>, <span class="hljs-number">3</span>): <span class="hljs-number">9</span>,
        (<span class="hljs-number">5</span>, <span class="hljs-number">4</span>): <span class="hljs-number">2</span>,
    }
    graph = {
        <span class="hljs-string">&#39;V&#39;</span>: V,
        <span class="hljs-string">&#39;E&#39;</span>: E
    }

    <span class="hljs-built_in">print</span>(dijkstra_min_distance(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, graph))
</code></pre>

<p>Prim算法求最小生成树</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># -*- coding: UTF-8 -*-</span>
<span class="hljs-string">&#39;&#39;&#39;
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll_108Prim算法求最小生成树.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/6/1 18:58             
   *****************************************
&#39;&#39;&#39;</span>

<span class="hljs-comment"># prim算法</span>
<span class="hljs-string">&#39;&#39;&#39;
核心：初始时从图中任取一顶点加入树T，此时树中只含有一个顶点，之后
选择一个与当前T中顶点集合距离最近的顶点，并将该顶点加入树T中，直到
所有顶点都被加入树T。
&#39;&#39;&#39;</span>
<span class="hljs-keyword">from</span> math <span class="hljs-keyword">import</span> inf

<span class="hljs-keyword">def</span> <span class="function_ hljs-title">prim_min_span_tree</span>(<span class="hljs-params">graph</span>):
    visited = {node: <span class="hljs-number">0</span> <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> graph}  <span class="hljs-comment"># 用于表示一个顶点是否被访问</span>
    root = <span class="hljs-number">1</span>  <span class="hljs-comment"># 任意取一个顶点</span>
    visited[root] = <span class="hljs-number">1</span>
    T_w = {}

    <span class="hljs-keyword">while</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">all</span>(visited.values()):  <span class="hljs-comment"># 只要不是所有的顶点被访问了，就一直进行下去</span>

        <span class="hljs-comment"># 查找与树T距离最近，但未被访问的顶点</span>
        not_visited_nodes = {node <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> graph <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> visited[node]}  <span class="hljs-comment"># 未被访问的顶点</span>
        visited_nodes = {node <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> graph <span class="hljs-keyword">if</span> visited[node]}  <span class="hljs-comment"># 树T</span>

        min_distance = inf
        min_node = <span class="hljs-literal">None</span>
        min_edge = <span class="hljs-literal">None</span>

        <span class="hljs-comment"># 求到树T距离最近的节点</span>
        <span class="hljs-keyword">for</span> t <span class="hljs-keyword">in</span> visited_nodes:
            <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> not_visited_nodes:
                cur_edge = <span class="hljs-string">&#39;-&#39;</span>.join(<span class="hljs-built_in">map</span>(<span class="hljs-built_in">str</span>, <span class="hljs-built_in">sorted</span>((t, node))))
                cur_w = W.get(cur_edge, -<span class="hljs-number">1</span>)  <span class="hljs-comment"># 当前边的权重</span>
                <span class="hljs-keyword">if</span> cur_w != -<span class="hljs-number">1</span> <span class="hljs-keyword">and</span> cur_w &lt; min_distance:
                    min_distance = cur_w
                    min_node = node
                    min_edge = cur_edge

        <span class="hljs-built_in">print</span>(<span class="hljs-string">f&#39;当前距离树T最近的节点:<span class="hljs-subst">{min_node}</span>,权重为:<span class="hljs-subst">{min_distance}</span>&#39;</span>)
        T_w[min_edge] = min_distance  <span class="hljs-comment"># 添加到树T的权重记录表中</span>
        visited[min_node] = <span class="hljs-number">1</span>  <span class="hljs-comment"># 更新当前节点为已访问</span>
    <span class="hljs-built_in">print</span>(T_w)


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    <span class="hljs-comment"># 邻接表法表示图</span>
    graph = {
        <span class="hljs-number">1</span>: {<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>},
        <span class="hljs-number">2</span>: {<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>},
        <span class="hljs-number">3</span>: {<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>},
        <span class="hljs-number">4</span>: {<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>},
        <span class="hljs-number">5</span>: {<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>},
        <span class="hljs-number">6</span>: {<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>}
    }

    W = {
        <span class="hljs-string">&#39;1-2&#39;</span>: <span class="hljs-number">6</span>,
        <span class="hljs-string">&#39;1-3&#39;</span>: <span class="hljs-number">1</span>,
        <span class="hljs-string">&#39;1-4&#39;</span>: <span class="hljs-number">5</span>,
        <span class="hljs-string">&#39;2-3&#39;</span>: <span class="hljs-number">5</span>,
        <span class="hljs-string">&#39;2-5&#39;</span>: <span class="hljs-number">3</span>,
        <span class="hljs-string">&#39;3-4&#39;</span>: <span class="hljs-number">5</span>,
        <span class="hljs-string">&#39;3-5&#39;</span>: <span class="hljs-number">6</span>,
        <span class="hljs-string">&#39;3-6&#39;</span>: <span class="hljs-number">4</span>,
        <span class="hljs-string">&#39;4-6&#39;</span>: <span class="hljs-number">2</span>,
        <span class="hljs-string">&#39;5-6&#39;</span>: <span class="hljs-number">6</span>
    }  <span class="hljs-comment"># 权重</span>
    <span class="hljs-built_in">print</span>(prim_min_span_tree(graph))
</code></pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

