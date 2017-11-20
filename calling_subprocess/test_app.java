
public class test_app
{
    public static void main(String[] args)
    {
        int time0 = 999999;
        int time1 = 999999;
        while(time0 > 1)
        {
            while(time1 > 1)
            {
                --time1;
                System.out.print(".");
            }
            time0--;
        }
    }
}
