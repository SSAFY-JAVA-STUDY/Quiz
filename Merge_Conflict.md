깃허브에 올라간 버전이 내 로컬 버전보다 나중 버전일 때는
해당 버전을 pull 하지 않고 내 버전을 push 할 수 없습니다. <br>

내용을 수정하겠습니다.

``` java
import java.util.Scanner;  
import java.util.*;  
import java.io.*;  
public class Main {  
    public static void main(String[] args) throws IOException {  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
  
        int N = Integer.parseInt(br.readLine());//홀수가 보장됨  
  
        int level = 0;  
        int mid = N/2;  
        boolean turn = false;  
        for (int i = 0; i < N; i++) {  
            for (int j = 0; j < N; j++) {  
                if(j<mid-level) System.out.print(" ");  
                else if(j>mid+level) System.out.print(" ");  
                else System.out.print("*");  
            }  
            System.out.println();  
            if(i==mid)turn=true;  
  
            if(!turn)level++;  
            else level--;  
  
        }  
    }  
}
```


내용을 추가 수정하겠습니다.