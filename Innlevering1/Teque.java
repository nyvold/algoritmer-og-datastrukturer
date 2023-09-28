package Innlevering1;

import java.io.*;
import java.lang.ArrayIndexOutOfBoundsException;

public class Teque {
    public Node first, last;

    protected class Node{
        public int data;
        public Node next;

        public Node(int data){
            this.data = data;
        }
    }
    public void push_front(int x){
        Node nynode = new Node(x);

        if (first == null){
            first = last = nynode;
        } 
        else{
            nynode.next = first;
            first = nynode;
        } 
    }

    public void push_back(int x){
        Node nynode = new Node(x);

        if (first == null) {
            first = last = nynode;
        }
        else if (first == last){
            last = nynode;
            first.next = nynode;
        }
        else{
            last.next = nynode;
            last = nynode;
        }
    }

    public void push_toIndex(int x, int index){
        Node nynode = new Node(x);
        if (index < 0 || index > size()){
            throw new ArrayIndexOutOfBoundsException(index);
        }

        Node node = first;
        Node forrige = null;
            for (int i = 0; i < index; i++) {
                forrige = node;
                node = node.next;
            }
            forrige.next = nynode;
            nynode.next = node;
    }

    public void push_middle(int x){
        Node nynode = new Node(x);

        if (first == null){
            first = last = nynode;
        }
        int index = size();
        if ((index % 2) == 0){
            push_toIndex(x, index / 2);
        }
        else if ((index % 2) == 1){
            push_toIndex(x, (index / 2) + 1);
        }
    }

    public int size(){
        Node node = first;
        int teller = 0;
        while(node != null){
            teller++;
            node = node.next;
        }
        return teller;
    }


    public static void main(String[]args){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    }
}