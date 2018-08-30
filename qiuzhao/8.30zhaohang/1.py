import java.util.Scanner;

/**
 * Created by lenovo on 2018/8/30.
 */

public class Main {


    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        char[] ch = sc.nextLine().toCharArray();

        int[] a = new int[ch.length];
        int countSumAdd = 0;
        int countSumDel= 0;

        int sum =0;
        for(int i = 0;i<ch.length;i++) {
            if (ch[i]=='C') {
                a[i]=0;
            }
            else
                a[i]=1;

            sum = sum + a[i];
        }

        for(int i =0;i<ch.length;i++){
            for(int j =1;j<ch.length-i;j++){
                if(a[j-1]>a[j]){
                    int temp;
                    temp = a[j-1];
                    a[j-1] = a[j];
                    a[j]=temp;
                    countSumAdd++;
                }
            }
        }

        for(int i =0;i<ch.length;i++){
            for(int j =1;j<ch.length-i;j++){
                if(a[j-1]<a[j]){
                    int temp;
                    temp = a[j-1];
                    a[j-1] = a[j];
                    a[j]=temp;
                    countSumDel++;
                }
            }
        }

        if(countSumAdd>countSumDel){
            System.out.print(countSumDel);
        }
        else
            System.out.print(countSumAdd);
    }
}