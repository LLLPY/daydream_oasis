
<BlogInfo title="LeetCode之合并二叉树" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=60 category="leetcode100题" tag_list="['leetcode', 'dfs']" create_time="2022.06.28 22:13:12.258138" update_time="2022.06.28 22:13:12" />

^^^^^^^^^
<h1>&nbsp;题目</h1>

<blockquote>
<p>给你两棵二叉树： root1 和 root2 。</p>

<p>想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。</p>

<p>返回合并后的二叉树。</p>

<p>注意: 合并过程必须从两个树的根节点开始。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p class="img-center" data-widget="image"><span><img alt="" isbindedload="true" src="https://img-blog.csdnimg.cn/img_convert/4bf245546a152317d60a2f804a14a290.png" /><span title="点击并拖拽以改变尺寸">​</span></span></p>

<p><br />
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]<br />
输出：[3,4,5,5,4,null,7]<br />
示例 2：</p>

<p>输入：root1 = [1], root2 = [1,2]<br />
输出：[2,2]<br />
&nbsp;</p>

<p>提示：</p>

<p>两棵树中的节点数目在范围 [0, 2000] 内<br />
-104 &lt;= Node.val &lt;= 104</p>

<p>来源：力扣（LeetCode）<br />
链接：https://leetcode.cn/problems/merge-two-binary-trees<br />
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。</p>
</blockquote>

<h1>思路</h1>

<blockquote>
<pre>
# 将二叉树的对应位置进行合并
&#39;&#39;&#39;
三种情况:
    1.左子树和右子树都有值，则相加即可
    2.左（右）子树有值，右（左）子树无值，则只添加左子树
    3.左子树无值，右子树无值，则不添加

遍历到任何一颗节点都是这样的，因此可以使用递归，当遍历完当前节点后，可以
再分别递归遍历当前节点的左子树和右子树
&#39;&#39;&#39;</pre>
</blockquote>

<h1>源码</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"># Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -&gt; TreeNode:

        # 只要有一颗子树遍历完结，则另一颗子树剩下的全部返回
        if not root1: return root2
        if not root2: return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root
</code></pre>

<h1>通过截图</h1>

<p><img src="../media/image/2022/06/28/image-20220628221307-1.png" style="height:612px; width:1115px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

