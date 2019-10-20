
class Node(object):
    def __init__(self,item):
        '''
        单节点实现
        elem用来存放具体数据
        next用来存放下一个节点的位置
        :param item: 节点数据
        '''
        self.elem = item
        self.next = None

class SingleLinkList(object):
    def __init__(self,node = None):
        '''
        单链表实现
        :param node: 传入node节点，默认为空链表，不包含任何节点
        '''
        # 链表头部,头部即第一个节点
        self.__head = node

    def is_empty(self):
        '''
        判断是否为空链表
        :return:
        '''
        # 如果链表头部直接指向None，则为空链表
        if self.__head == None:
            return True
        else:
            return False

    def length(self):
        '''
        :return: 返回链表长度
        '''
        #首先游标停在链表的起始位置
        cur = self.__head
        #定义一个变量，用于长度计数
        count = 0
        while cur != None:
            count += 1
            # 移动游标到下一个节点
            cur = cur.next
        return count

    def travel(self):
        '''
        遍历链表
        :return:
        '''
        # 首先将游标定位到链表头部
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            # 游标向后移动
            cur = cur.next
        print("")

    def get_head(self):
        return self.__head

    def append(self,item):
        '''
        尾部添加节点
        :param item: 节点
        :return:
        '''
        node = Node(item)
        # 判断当前链表是否为空链表
        if self.is_empty():
            # 如果为空链表，直接附加新节点
            self.__head = node
        else:
            # 如果不为空链表，需要遍历当前链表中节点，找到最后一个节点
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self,item):
        '''
        在链表头部添加节点
        :param item:
        :return:
        '''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 如果节点不为空,先将头部节点链接到要头部插入节点的next区域,保证链不断
            node.next = self.__head
            # 将头部插入的节点连接到头部，即完成了头部插入
            self.__head = node

    def insert(self,pos,item):
        '''
        任意位置插入节点
        :param pos: 位置
        :param item: 节点
        :return:
        '''
        # 根据位置判断是头部插入、尾部插入、其他位置插入
        # 头部
        if pos <= 0:
            self.add(item)
        # 尾部
        elif pos >= self.length():
            self.append(item)
        #其他位置插入需要定义前一个节点的游标
        else:
            node = Node(item)
            # 起点游标
            pre = self.__head
            count = 0
            # 插入在位置前面
            while count < pos-1:
                pre = pre.next
                count += 1
            # 将插入节点的next区域指向原节点前一个节点的next区域
            node.next = pre.next
            # 将node指向前一个节点的next区域
            pre.next = node

    def remove(self,item):
        '''
        删除相应节点
        :param item: 节点数据
        :return:
        '''
        if self.is_empty():
            return
        else:
            # 需要定义两个游标
            pre = None
            cur = self.__head
            # 判断是否移动到单链表尾部
            while cur != None:
                # 没找到就继续向后查找
                if cur.elem != item:
                    pre = cur
                    cur = cur.next
                else:
                    # 头部删除
                    if cur == self.__head:
                        self.__head = cur.next
                    # 包含尾部删除
                    else:
                        pre.next = cur.next
                    break

    def search(self, item):
        # 查找节点是否存在
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == '__main__':
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    ll.add(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    ll.insert(2,22)
    ll.travel()
    ll.remove(4)
    ll.travel()
