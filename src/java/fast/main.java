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

        try {
            data = readFile("../../rounds.txt", StandardCharsets.UTF_8);
        } catch (IOException err) {
            System.out.println("Couldn't read file:\n" + err.getMessage());
        }

        int rounds = Integer.parseInt(data);

        boolean total[] = new boolean[rounds + 1];
        for (int i = 0; i < total.length; i++) {
            total[i] = true;
        }

        
        for (int i = 2; i <= Math.sqrt(rounds); i++) {
            if (total[i] == true) {
                for (int j = i * i; j < rounds; j += i) {
                    total[j] = false;
                }
            }
        }

        int primes = 0;
        for (int k = 2; k < rounds; k++) {
            if (total[k] == true) {
                primes++;
            }
        }
        int composites = rounds - primes;


        long end = System.nanoTime() - start;
        System.out.println(System.getProperty("java.version") + " " + (float)end / 1000000000);

    }


}

