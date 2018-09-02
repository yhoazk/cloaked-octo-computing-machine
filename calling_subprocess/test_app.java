
public class test_app
{
    public static void main(String[] args)
    {
        int total = 0;
        int time0 = 5;
        int time1 = 5;
        while(time0 > 0)
        {
            while(time1 > 0)
            {
                --time1;
                ++total;
                System.out.print(".");
            }
            time0--;
            time1 = 5;
        }
        System.exit(9);
    }
}
