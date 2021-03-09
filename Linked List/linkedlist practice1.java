public class Main {
    public static void main(String[] args){
    LinkedList li = new LinkedList();
    li.insert(23);
    li.insert(34);
        li.insertAtStart(2);
        li.insertAtStart(1);
        li.insertAt(0,33);
        li.deleteAt(1);
    li.show();
    }
}

//node class with data of type integer and next of type Node
class Node{
    int data;
    Node next;
}

//Main linkedlist class to which which will create node and perform various operations of linked list
class LinkedList{
    Node head;
    //it inserts the data at the end of the link list
    public void insert(int data){
        Node node = new Node();
        node.data = data;
        node.next = null;

        if (head == null){
            head = node;
        }
        else{
            Node n = head;
            while(n.next != null){
                n = n.next;
            }
            n.next = node;
        }
    }

    //It add data to starting of the linkedlist
    public void insertAtStart(int data){
        Node node = new Node();
        node.data = data;

        if (head == null){
            node.next = null;
            head = node;
        }
        else{
            node.next = head;
            head = node;

        }
    }

    //It adds the data at particular index
    public void insertAt(int index, int data){
        Node node = new Node();
        node.data = data;

        if(index ==0){
            insertAtStart(data);
        }
        else{
            Node n = head;
            for (int i = 0; i < index-1 ; i++) {
                n = n.next;
            }
            node.next = n.next;
            n.next = node;
        }
    }

    //It deletes the data at particular index
    public void deleteAt(int index){
        if(index == 0){
            head = head.next;
        }
        else{
            Node n = head;
            for (int i = 0; i < index-1 ; i++) {
                n = n.next;
            }
            n.next = n.next.next;
        }
    }


    //print the data of linkedlist
    public void show(){
        Node show = head;
        while(show.next != null){
            System.out.println(show.data);
            show = show.next;
        }
        System.out.println(show.data);
    }
}
