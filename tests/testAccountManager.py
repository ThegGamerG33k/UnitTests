import src.AccountManager as AccountManager
from unittest import TestCase

class Tester(TestCase):
    @classmethod
    def setUpClass(cls):
        Tester.A = AccountManager.AccountManager()
        Tester.A.addUser( "Alice", "qwerty")



    #verifyUser Tests
    def test_verifyUser(self):
        A = Tester.A
        self.assertFalse( A.verifyUser( "Jouce", "s3cr3t"), 
                         "Should return false if user does not exists")
        self.assertFalse( A.verifyUser( "Alice", "wrong"),
                         "Should return false if the Password doesn't match")
        
    def test_verifyUser2(self):
        A = Tester.A
        self.assertTrue( A.verifyUser( "Alice", "qwerty"),
                        "Should return True if user does exist and password does match")
        
    def test_verifyUser3(self):
        A = Tester.A
        self.assertRaises( Exception, A.verifyUser, 1, 2)
        self.assertRaises( Exception, A.verifyUser, 1.1, 2.2)



    #addUser Tests
    def test_addUser(self):
        A = Tester.A
        self.assertRaises( Exception, A.addUser, 1, 1)
        self.assertRaises( Exception, A.addUser, 1.1, 2.2)

    def test_addUser2(self):
        A = Tester.A
        self.assertTrue( A.addUser( "bob", "s3cr3t"),
                        "Should return true if user is added")
        self.assertFalse( A.addUser( "Alice", "qwerty"),
                         "Should return false if the user already exists")
        self.assertFalse( A.addUser( "" , "secret"),
                         "Should return false if no user was provided")
        self.assertFalse( A.addUser( "scarlet", ""),
                         "Should return false if no password was given")
        self.assertRaises( Exception, A.addUser, "shawn", 3)
        self.assertRaises( Exception, A.addUser, "shawn", 3.1)
        self.assertRaises( Exception, A.addUser, 1, "password")
        self.assertRaises( Exception, A.addUser, 1.1, "password")

    def test_addUser3(self):
        A = Tester.A
        self.assertFalse( A.isAdmin(A.getUID("Alice")), 
                         "Should return false as new user should not be admins")
        self.assertFalse( A.isAdmin( A.getUID("bob")),
                         "Should return false as new user should not be admins")
        


    #getUID Tests
    def test_getUID(self):
        A = Tester.A
        self.assertRaises( Exception, A.getUID, 1)
        self.assertRaises( Exception, A.getUID, 1.1)
        self.assertIsNone( A.getUID("juan"))
    
    def test_getUID2(self):
        A = Tester.A
        self.assertGreaterEqual( A.getUID("Alice"), 0)
        self.assertGreaterEqual( A.getUID("bob"), 0)
        self.assertNotEqual( A.getUID("Alice"), A.getUID("bob"))
        


    #isAdmin Tests
    def test_isAdmin(self):
        A = Tester.A
        self.assertRaises( Exception, A.isAdmin, "string")
        self.assertRaises( Exception, A.isAdmin, 1.1)

    def test_isAdmin2(self):
        A = Tester.A
        A.setAdmin(A.getUID("Alice"), True)
        self.assertTrue( A.isAdmin( A.getUID("Alice") ),
                         "Should return true if this user is an admin")
        self.assertFalse( A.isAdmin( A.getUID( "bob")),
                         "Should return false if the user is not an admin")
        self.assertFalse( A.isAdmin( 100000000000000 ),
                         "Should return false if it's a bad user ID")



    #setAdmin Tests
    def test_setAdmin(self):
        A = Tester.A
        self.assertRaises( Exception, A.setAdmin, "string", True)
        self.assertRaises( Exception, A.setAdmin, 1.1, False)
        self.assertRaises( Exception, A.setAdmin, A.getUID("Alice"), 1)
        self.assertRaises( Exception, A.setAdmin, A.getUID("Alice"), 1.1)

    def test_setAdmin2(self):
        A = Tester.A
        self.assertTrue( A.setAdmin(A.getUID("Alice"), True), 
                        "Should return true if the user is made an admin when the second condition is true")
        self.assertTrue( A.setAdmin(A.getUID("Alice"), False),
                        "Should return true if the user was an admin and has been removed from being admin")
        self.assertFalse( A.setAdmin( 1000000000000, True),
                        "Should return false if the userID doesn't correspond to a known user")
        self.assertFalse( A.setAdmin( 1000000000000, False),
                        "Should return false if the userID doesn't correspond to a known user")


    