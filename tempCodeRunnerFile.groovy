public class Solution {
    public static int waitingTime(tickets, p){
        List result = new ArrayList();
        for (int i = 0; i < tickets.length; i++){
            if(i<=p){
                result.add(Math.min(tickets[i], tickets[p]))
            }
            else{
                result.add(Math.min(tickets[i], tickets[p] - 1))
            }
        }
        return result.sum()
    }
    
}
