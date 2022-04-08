import java.nio.charset.Charset;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;

public class main {
    static String readFile(String path, Charset encoding) throws IOException {
        byte[] encoded = Files.readAllBytes(Paths.get(path));
        return new String(encoded, encoding);
    }

    public static void main(String[] args) {
        long start = System.nanoTime();

        String data = "";
        int primes = 0, composites = 0;

        try {
            data = readFile("../../rounds.txt", StandardCharsets.UTF_8);
        } catch (IOException err) {
            System.out.println("Couldn't read file:\n" + err.getMessage());
        }

        int rounds = Integer.parseInt(data);

        for(int num = 0; num <= rounds; num++) {
            int ctr = 0;

            for(int i = 2; i <= num / 2; i++) {
                if(num % i == 0) {
                    ctr++;
                    composites++;
                    break;
                }
            }

            if(ctr == 0 && num != 1) {
                primes++;
            }
        }

        long end = System.nanoTime() - start;
        System.out.println(System.getProperty("java.version") + " " + (float)end / 1000000000);

    }


}
