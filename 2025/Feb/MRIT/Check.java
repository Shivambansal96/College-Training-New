import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class Check {
    public static void main(String[] args) {
		String driver="com.mysql.jdbc.Driver";
		String url = "jdbc:mysql://localhost:3306/shivam";
		String userName = "root";
		String password = "root";

        try {
            // Loading the Driver
            Class.forName(driver);
            
            //jdbc connection
            Connection con= DriverManager.getConnection(url, userName, password);
            System.out.println(con);
            PreparedStatement pst = con.prepareStatement("CREATE DATABASE Shivam");
            int i = pst.executeUpdate();
            System.out.println(i);
        }

        catch(Exception e) {
            e.printStackTrace();

        }
	}
}