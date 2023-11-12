---

next: false

---



<BlogInfo id="1360"/>

```c#
using System;

namespace paixuCS

{

    class Program

    {

        using System;

namespace Sorting_algorithm

{

    // 选择排序

    public static void SelectSort(IList<int> data)

        {

            for (int i = 0; i < data.Count - 1; i++)

            {

                int min = i;

                int temp = data[i];

                for (int j = i + 1; j < data.Count; j++)

                {

                    if (data[j] < temp)

                    {

                        min = j;

                        temp = data[j];

                    }

                }

                if (min != i)

                    Swap(data, min, i);

            }

        }

//   冒泡排序

public static void BubbleSort(IList<int> data)

        {

            for (int i = data.Count - 1; i > 0; i--)

            {

                for (int j = 0; j < i; j++)

                {

                    if (data[j] > data[j + 1])

                        Swap(data, j, j + 1);

                }

            }

        }

        // 通过表示提升冒泡排序

        public static void BubbleSortImprovedWithFlag(IList<int> data)

        {

            bool flag;

            for (int i = data.Count - 1; i > 0; i--)

            {

                flag = true;

                for (int j = 0; j < i; j++)

                {

                    if (data[j] > data[j + 1])

                    {

                        Swap(data, j, j + 1);

                        flag = false;

                    }

                }

                if (flag) break;

            }

        }

        // 来回排序 冒泡排序的更高优化

        public static void BubbleCocktailSort(IList<int> data)

        {

            bool flag;

            int m = 0, n = 0;

            for (int i = data.Count - 1; i > 0; i--)

            {

                flag = true;

                if (i % 2 == 0)

                {

                    for (int j = n; j < data.Count - 1 - m; j++)

                    {

                        if (data[j] > data[j + 1])

                        {

                            Swap(data, j, j + 1);

                            flag = false;

                        }

                    }

                    if (flag) break;

                    m++;

                }

                else

                {

                    for (int k = data.Count - 1 - m; k > n; k--)

                    {

                        if (data[k] < data[k - 1])

                        {

                            Swap(data, k, k - 1);

                            flag = false;

                        }

                    }

                    if (flag) break;

                    n++;

                }

            }

        }

        // 插入排序

        public static void InsertSort(IList<int> data)

        {

            int temp;

            for (int i = 1; i < data.Count; i++)

            {

                temp = data[i];

                for (int j = i - 1; j >= 0; j--)

                {

                    if (data[j] > temp)

                    {

                        data[j + 1] = data[j];

                        if (j == 0)

                        {

                            data[0] = temp;

                            break;

                        }

                    }

                    else

                    {

                        data[j + 1] = temp;

                        break;

                    }

                }

            }

        }

        // 二分查找优化插入排序

        public static void InsertSortImprovedWithBinarySearch(IList<int> data)

        {

            int temp;

            int tempIndex;

            for (int i = 1; i < data.Count; i++)

            {

                temp = data[i];

                tempIndex = BinarySearchForInsertSort(data, 0, i, i);

                for (int j = i - 1; j >= tempIndex; j--)

                {

                    data[j + 1] = data[j];

                }

                data[tempIndex] = temp;

            }

        }

        public static int BinarySearchForInsertSort(IList<int> data, int low, int high, int key)

        {

            if (low >= data.Count - 1)

                return data.Count - 1;

            if (high <= 0)

                return 0;

            int mid = (low + high) / 2;

            if (mid == key) return mid;

            if (data[key] > data[mid])

            {

                if (data[key] < data[mid + 1])

                    return mid + 1;

                return BinarySearchForInsertSort(data, mid + 1, high, key);

            }

            else  // data[key] <= data[mid]

            {

                if (mid - 1 < 0) return 0;

                if (data[key] > data[mid - 1])

                    return mid;

                return BinarySearchForInsertSort(data, low, mid - 1, key);

            }

        }

        // 快速排序第一版

        public static void QuickSortStrict(IList<int> data)

        {

            QuickSortStrict(data, 0, data.Count - 1);

        }

        public static void QuickSortStrict(IList<int> data, int low, int high)

        {

            if (low >= high) return;

            int temp = data[low];

            int i = low + 1, j = high;

            while (true)

            {

                while (data[j] > temp) j--;

                while (data[i] < temp && i < j) i++;

                if (i >= j) break;

                Swap(data, i, j);

                i++; j--;

            }

            if (j != low)

                Swap(data, low, j);

            QuickSortStrict(data, j + 1, high);

            QuickSortStrict(data, low, j - 1);

        }

        // 快速排序另一版本

        public static void QuickSortRelax(IList<int> data)

        {

            QuickSortRelax(data, 0, data.Count - 1);

        }

        public static void QuickSortRelax(IList<int> data, int low, int high)

        {

            if (low >= high) return;

            int temp = data[(low + high) / 2];

            int i = low - 1, j = high + 1;

            while (true)

            {

                while (data[++i] < temp) ;

                while (data[--j] > temp) ;

                if (i >= j) break;

                Swap(data, i, j);

            }

            QuickSortRelax(data, j + 1, high);

            QuickSortRelax(data, low, i - 1);

        }

        // 快排的优化

        public static void QuickSortRelaxImproved(IList<int> data)

        {

            QuickSortRelaxImproved(data, 0, data.Count - 1);

        }

        public static void QuickSortRelaxImproved(IList<int> data, int low, int high)

        {

            if (low >= high) return;

            int temp = data[(low + high) / 2];

            int i = low - 1, j = high + 1;

            int index = (low + high) / 2;

            while (true)

            {

                while (data[++i] < temp) ;

                while (data[--j] > temp) ;

                if (i >= j) break;

                Swap(data, i, j);

                if (i == index) index = j;

                else if (j == index) index = i;

            }

            if (j == i)

            {

                QuickSortRelaxImproved(data, j + 1, high);

                QuickSortRelaxImproved(data, low, i - 1);

            }

            else //i-j==1

            {

                if (index >= i)

                {

                    if (index != i)

                        Swap(data, index, i);

                    QuickSortRelaxImproved(data, i + 1, high);

                    QuickSortRelaxImproved(data, low, i - 1);

                }

                else //index < i

                {

                    if (index != j)

                        Swap(data, index, j);

                    QuickSortRelaxImproved(data, j + 1, high);

                    QuickSortRelaxImproved(data, low, j - 1);

                }

            }

        }

        // 归并排序

        public static List<int> MergeSortOnlyList(List<int> data, int low, int high)

        {

            if (low == high)

                return new List<int> { data[low] };

            List<int> mergeData = new List<int>();

            int mid = (low + high) / 2;

            List<int> leftData = MergeSortOnlyList(data, low, mid);

            List<int> rightData = MergeSortOnlyList(data, mid + 1, high);

            int i = 0, j = 0;

            while (true)

            {

                if (leftData[i] < rightData[j])

                {

                    mergeData.Add(leftData[i]);

                    if (++i == leftData.Count)

                    {

                        mergeData.AddRange(rightData.GetRange(j, rightData.Count - j));

                        break;

                    }

                }

                else

                {

                    mergeData.Add(rightData[j]);

                    if (++j == rightData.Count)

                    {

                        mergeData.AddRange(leftData.GetRange(i, leftData.Count - i));

                        break;

                    }

                }

            }

            return mergeData;

        }

        public static List<int> MergeSortOnlyList(List<int> data)

        {

            data = MergeSortOnlyList(data, 0, data.Count - 1);  //不会改变外部引用 参照C#参数传递

            return data;

        }

        // 新版本的归并排序

        public static IList<int> MergeSort(IList<int> data)

        {

            data = MergeSort(data, 0, data.Count - 1);

            return data;

        }

        public static IList<int> MergeSort(IList<int> data, int low, int high)

        {

            int length = high - low + 1;

            IList<int> mergeData = NewInstance(data, length);

            if (low == high)

            {

                mergeData[0] = data[low];

                return mergeData;

            }

            int mid = (low + high) / 2;

            IList<int> leftData = MergeSort(data, low, mid);

            IList<int> rightData = MergeSort(data, mid + 1, high);

            int i = 0, j = 0;

            while (true)

            {

                if (leftData[i] < rightData[j])

                {

                    mergeData[i + j] = leftData[i++]; //不能使用Add,Array Length不可变

                    if (i == leftData.Count)

                    {

                        int rightLeft = rightData.Count - j;

                        for (int m = 0; m < rightLeft; m++)

                        {

                            mergeData[i + j] = rightData[j++];

                        }

                        break;

                    }

                }

                else

                {

                    mergeData[i + j] = rightData[j++];

                    if (j == rightData.Count)

                    {

                        int leftleft = leftData.Count - i;

                        for (int n = 0; n < leftleft; n++)

                        {

                            mergeData[i + j] = leftData[i++];

                        }

                        break;

                    }

                }

            }

            return mergeData;

        }

        // 堆排序

        public static void HeapSort(IList<int> data)

        {

            BuildMaxHeapify(data);

            int j = data.Count;

            for (int i = 0; i < j; )

            {

                Swap(data, i, --j);

                if (j - 2 < 0)  //只剩下1个数 j代表余下要排列的数的个数

                    break;

                int k = 0;

                while (true)

                {

                    if (k > (j - 2) / 2) break;  //即：k > ((j-1)-1)/2 超出最后一个父节点的位置

                    else

                    {

                        int temp = k;

                        k = ReSortMaxBranch(data, k, 2 * k + 1, 2 * k + 2, j - 1);

                        if (temp == k) break;

                    }

                }

            }

        }

        public static void BuildMaxHeapify(IList<int> data)

        {

            for (int i = data.Count / 2 - 1; i >= 0; i--)  //(data.Count-1)-1)/2为数列最大父节点索引

            {

                int temp = i;

                temp = ReSortMaxBranch(data, i, 2 * i + 1, 2 * i + 2, data.Count - 1);

                if (temp != i)

                {

                    int k = i;

                    while (k != temp && temp <= data.Count / 2 - 1)

                    {

                        k = temp;

                        temp = ReSortMaxBranch(data, temp, 2 * temp + 1, 2 * temp + 2, data.Count - 1);

                    }

                }

            }

        }

        public static int ReSortMaxBranch(IList<int> data, int maxIndex, int left, int right, int lastIndex)

        {

            int temp;

            if (right > lastIndex)  //父节点只有一个子节点

                temp = left;

            else

            {

                if (data[left] > data[right])

                    temp = left;

                else temp = right;

            }

            if (data[maxIndex] < data[temp])

                Swap(data, maxIndex, temp);

            else temp = maxIndex;

            return temp;

        }

        // 希尔排序

        public static void ShellSort(IList<int> data)

        {

            int temp;

            for (int gap = data.Count / 2; gap > 0; gap /= 2)

            {

                for (int i = gap; i < data.Count; i += gap)

                {

                    temp = data[i];

                    for (int j = i - gap; j >= 0; j -= gap)

                    {

                        if (data[j] > temp)

                        {

                            data[j + gap] = data[j];

                            if (j == 0)

                            {

                                data[j] = temp;

                                break;

                            }

                        }

                        else

                        {

                            data[j + gap] = temp;

                            break;

                        }

                    }

                }

            }

        }

        // 希尔排序优化

        public static void ShellSortCorrect(IList<int> data)

        {

            int temp;

            for (int gap = data.Count / 2; gap > 0; gap /= 2)

            {

                for (int i = gap; i < data.Count; i++)      // i+ = gap 改为了 i++

                {

                    temp = data[i];

                    for (int j = i - gap; j >= 0; j -= gap)

                    {

                        if (data[j] > temp)

                        {

                            data[j + gap] = data[j];

                            if (j == 0)

                            {

                                data[j] = temp;

                                break;

                            }

                        }

                        else

                        {

                            data[j + gap] = temp;

                            break;

                        }

                    }

                }

            }

        }

        // 桶排序

          public static void BucketSortOnlyUnitDigit(IList<int> data)

          {

              int[] indexCounter = new int[10];

              for (int i = 0; i < data.Count; i++)

              {

                  indexCounter[data[i]]++;

              }

              int[] indexBegin = new int[10];

              for (int i = 1; i < 10; i++)

             {

                 indexBegin[i] = indexBegin[i-1]+ indexCounter[i-1];

             }

             IList<int> tempList = NewInstance(data, data.Count);

             for (int i = 0; i < data.Count; i++)

             {

                 int number = data[i];

                 tempList[indexBegin[number]++] = data[i];

             }

             data = tempList;

         }

        //  桶排序2

        public static IList<int> RadixSort(IList<int> data)

        {

            int max = data[0];

            for (int i = 1; i < data.Count; i++)

            {

                if (data[i] > max)

                    max = data[i];

            }

            int digit = 1;

            while (max / 10 != 0)

            {

                digit++;

                max /= 10;

            }

            for (int i = 0; i < digit; i++)

            {

                int[] indexCounter = new int[10];

                IList<int> tempList = NewInstance(data, data.Count);

                for (int j = 0; j < data.Count; j++)

                {

                    int number = (data[j] % Convert.ToInt32(Math.Pow(10, i + 1))) / Convert.ToInt32(Math.Pow(10, i));  //得出i+1位上的数

                    indexCounter[number]++;

                }

                int[] indexBegin = new int[10];

                for (int k = 1; k < 10; k++)

                {

                    indexBegin[k] = indexBegin[k - 1] + indexCounter[k - 1];

                }

                for (int k = 0; k < data.Count; k++)

                {

                    int number = (data[k] % Convert.ToInt32(Math.Pow(10, i + 1))) / Convert.ToInt32(Math.Pow(10, i));

                    tempList[indexBegin[number]++] = data[k];

                }

                data = tempList;

            }

            return data;

        }

        // 测试代码

        public static int[] RandomSet(int length, int max)

        {

            int[] result = new int[length];

            Random rand = new Random();

            for (int i = 0; i < result.Length; i++)

            {

                result[i] = rand.Next(max);

            }

            return result;

        }

        public static bool IsAscOrdered(IList<int> data)

        {

            bool flag = true;

            for (int i = 0; i < data.Count - 1; i++)

            {

                if (data[i] > data[i + 1])

                    flag = false;

            }

            return flag;

        }

        public static void TestMicrosoft(IList<int> data)

        {

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();

            List<int> result = data.OrderBy(a => a).ToList();

            stopwatch.Stop();

            string methodName = "TestMicrosoft";

            int length = methodName.Length;

            for (int i = 0; i < 40 - length; i++)

            {

                methodName += " ";

            }

            Console.WriteLine(methodName +

                "  IsAscOrdered:" + IsAscOrdered(result) + "  Time:" + stopwatch.Elapsed.TotalSeconds);

        }

    //  测试 主体

    static void Main(string[] args)

        {

            int[] aa = RandomSet(50000, 99999);

            //int[] aa = OrderedSet(5000);

            Console.WriteLine("Array Length:" + aa.Length);

            RunTheMethod((Action<IList<int>>)SelectSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)BubbleSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)BubbleSortImprovedWithFlag, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)BubbleCocktailSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)InsertSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)InsertSortImprovedWithBinarySearch, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)QuickSortStrict, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)QuickSortRelax, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)QuickSortRelaxImproved, aa.Clone() as int[]);

            RunTheMethod((Func<IList<int>, IList<int>>)MergeSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)ShellSort, aa.Clone() as int[]);

            RunTheMethod((Func<IList<int>, IList<int>>)RadixSort, aa.Clone() as int[]);

            RunTheMethod((Action<IList<int>>)HeapSort, aa.Clone() as int[]);

            TestMicrosoft(aa.Clone() as int[]);

            Console.Read();

        }

        public static void RunTheMethod(Func<IList<int>, IList<int>> method, IList<int> data)

        {

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();

            IList<int> result = method(data);

            stopwatch.Stop();

            string methodName = method.Method.Name;

            int length = methodName.Length;

            for (int i = 0; i < 40 - length; i++)

            {

                methodName += " ";

            }

            Console.WriteLine(methodName +

                "  IsAscOrdered:" + IsAscOrdered(result) + "  Time:" + stopwatch.Elapsed.TotalSeconds);

        }

        public static void RunTheMethod(Action<IList<int>> method, IList<int> data)

        {

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();

            method(data);

            stopwatch.Stop();

            string methodName = method.Method.Name;

            int length = methodName.Length;

            for (int i = 0; i < 40 - length; i++)

            {

                methodName += " ";

            }

            Console.WriteLine(methodName +

                "  IsAscOrdered:" + IsAscOrdered(data) + "  Time:" + stopwatch.Elapsed.TotalSeconds);

        }

}

    }

}
```
  





<ActionBox />
