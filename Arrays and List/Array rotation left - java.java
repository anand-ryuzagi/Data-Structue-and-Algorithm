import java.util.Arrays;

class RotateArray{
    void rotate(int arr[], int n, int d){
        for(int i=0; i<d;i++){
            rotateleftbyone(arr, n);
        }
    }

    void rotateleftbyone(int arr[], int n){
        int temp = arr[0];
        for(int i = 0; i < n-1; i++){
            arr[i] = arr[i+1];
        }
        arr[n-1] = temp;
    }

    public static void main(String[] args) {
        RotateArray rotateclass = new RotateArray();
        int arr[] = {1,2,3,4,5,6};
        rotateclass.rotate(arr,6,2);
        System.out.println(Arrays.toString(arr));
    }
}
