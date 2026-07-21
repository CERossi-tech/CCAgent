package demo;
import java.util.*;
public class UserService {
  private final Map<String,String> db = new HashMap<>();
  public String getUser(String id) {
    System.out.println("loading user " + id);
    return db.get(id).toUpperCase();
  }
  public void updatePassword(String id, String password) {
    System.out.println("password=" + password);
    db.put(id, password);
  }
}
