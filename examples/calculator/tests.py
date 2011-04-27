from pulsar import test
from pulsar.http import rpc

from .manage import server

class TestRpcMeta(test.TestCase):
    
    def testHandler(self):
        s = server()
        self.assertTrue(s.callable)
        handler = s.callable
        self.assertEqual(handler.content_type,'text/json')
        self.assertEqual(handler.route,'/')
        self.assertEqual(len(handler.subHandlers),1)

#class TestCalculatorExample(test.TestCase):
class _TestCalculatorExample(object):
    
    def initTests(self):
        return self.suiterunner.run(start_server,
                                    concurrency = 'process',
                                    parse_console = False)
        
    def endTests(self):
        pass
        #self.server.stop()
        
    def setUp(self):
        self.p = rpc.JsonProxy('http://localhost:8060')
        
    def testPing(self):
        result = self.p.ping()
        self.assertEqual(result,'pong')
        
    def testAdd(self):
        result = self.p.add(3,7)
        self.assertEqual(result,10)
        
    def testSubtract(self):
        result = self.p.subtract(546,46)
        self.assertEqual(result,500)
        
    def testMultiply(self):
        result = self.p.multiply(3,9)
        self.assertEqual(result,27)
        
    def testDivide(self):
        result = self.p.divide(50,25)
        self.assertEqual(result,2)
        
    def testInfo(self):
        result = self.p.server_info()
        self.assertTrue('server' in result)
        server = result['server']
        self.assertTrue('version' in server)
        
    def testInvalidParams(self):
        self.assertRaises(rpc.InvalidParams,self.p.divide,50,25,67)
        
    def testInvalidFunction(self):
        self.assertRaises(rpc.NoSuchFunction,self.p.foo,'ciao')
        

