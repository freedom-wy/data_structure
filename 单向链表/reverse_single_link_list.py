class ListNode:  # 定义一个对象(结构体)
    def __init__(self, x):
        self.val = x
        self.next = None


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head
    pre = None  # 记录上一个节点,初始化为None
    cur = head
    while cur:
        tmp = cur.next  # 保留记录下一个节点的位置
        cur.next = pre  # 更改当前的节点中的next为上一个节点(第一次头节点为None)
        pre = cur  # 将当前节点赋值给pre,为了赋值给下一个节点的next,实现逆序
        cur = tmp  # 将当前节点重置为当前节点的下一个节点
        # 简化:
        # cur.next, pre, cur = pre, cur, cur.next
    return pre


head = ListNode(1)  # 测试代码
p1 = ListNode(2)  # 建立链表1->2->3->4->None
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
p = nonrecurse(head)  # 输出链表 4->3->2->1->None
while p:
    print(p.val)
    p = p.next