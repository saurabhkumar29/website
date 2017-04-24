import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/PLG")

public class PLG extends HttpServlet 
{
 	 PrintWriter out;
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException 
    {
        out = resp.getWriter();
        String s1 = req.getParameter("s1");
        String s2 = req.getParameter("s2");
        
        CompareString(s1,s2);
        out.close();
    }
    
    public void CompareString(String A,String B)
    {
    String[] wordsA = A.split("\\s");
    String[] wordsB = B.split("\\s");
    int c=0;
    for(int i=0; i<wordsA.length;i++)
    {
        for(int j=0;j<wordsB.length;j++)
        {
        if(wordsA[i].equals(wordsB[j]))
        {
        c++;
        }
        }
    }
    
    double common;
    if(wordsA.length>wordsB.length)
    {
        common = ((double)c/(double)wordsA.length)*100;
    }
    else
    {
        common = ((double)c/(double)wordsB.length)*100;
    }

    
    double uniq = 100-common;
    out.println("Uniqueness is"+ (float)uniq+"% ");
    if(uniq>65)
    {
    out.print("No plagiarism detected...");
    }
    else
    {
    out.print("PLagiarism Detected... You are cheater...");
    }
    }
}