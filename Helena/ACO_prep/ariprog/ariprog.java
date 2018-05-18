/*
ID: helenaz1
LANG: JAVA
TASK: ariprog
*/
import java.util.*;
import java.io.*;
public class ariprog{
    static int N;
    static int M;
    public static void main(String [] args) throws IOException{
        Scanner scan = new Scanner(new File("ariprog.in"));
        PrintWriter write = new PrintWriter(new File("ariprog.out");
        N = scan.nextInt();
        M = scan.nextInt();
        List<Pair>pairs = new ArrayList<Pair>();
        int[] sequence = new int[M*M*2+1];
        for (int i = 0; i <= M; i++){
            for (int j = i; j<=M;j++){
                sequence[j*j+i*i] = 1;
            }
        }
        int large = (M*M*2)/(N-1)+1;
        for (int i = 1; i<large;i++){
            for (int j = 0; j<sequence.length(); j++){
                if (sequence[j] == 1){
                    boolean complete = true
                    for (int k = 1; k<N,k++){
                        if (j+i*k > 2*M*M || sequence[j+i*k] == 0){
                            complete = false;
                            break;
                        }
                    if complete{
                        pairs.add(new Pair(j,i))
                    }
                    
                    }
                }
            }
        }
        if (pairs.size() == 0){
            write.println("NONE");
        }
        else{
            for (Pair a : pairs){
                write.println(a.get(0)+" "+a.get(1))
            }
        }
        scan.close()
        write.close()
    }
}