//time complexity = O(n)
//space complexity = O(1)

import java.util.Arrays;

class Main{
    void rotate(int arr[], int n, int d){
        int j, k,temp;
        int gcd = gcd(d,n);
        for(int i=0; i<gcd;i++){
            temp = arr[i];
            j = i;
            while(true){
                k = j+d;
                if (k >= n)
                    k = k-n;
                if(k==i)
                    break;
                arr[j] = arr[k];
                j=k;
            }
            arr[j] = temp;

        }
    }

    int gcd(int a, int b){
        if(b==0)
            return a;
        else
            return gcd(b,a%b);
    }

    public static void main(String[] args) {
        Main rotateclass = new Main();
        int arr[] = {1,2,3,4,5,6,7,8};
        rotateclass.rotate(arr,8,2);
        System.out.println(Arrays.toString(arr));
    }
}

