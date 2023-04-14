import unittest
import mappsite.helpers
import treelib as tr


class TestHelpers(unittest.TestCase):
    def test_connection_no_redirections(self):
        url = "http://google.com"
        outcome, tree = mappsite.helpers.test_connection(url, "search?q=:)")
        self.assertEqual(outcome, True)

    def test_connection_redirections(self):
        url = "http://httpbin.org"
        outcome, tree = mappsite.helpers.test_connection(url, "relative-redirect/4", )
        self.assertEqual(outcome, True)
        self.assertNotEqual(tree, None)
        tree.show()

    def test_link_cat(self):
        tree = tr.Tree()
        tree.create_node("https://www.polimi.it", "https://www.polimi.it")
        tree.create_node("il-politecnico", "il-politecnico", parent="https://www.polimi.it")
        tree.create_node("chi-siamo", "chi-siamo", parent="il-politecnico")
        tree.create_node("i-nostri-valori", "i-nostri-valori", parent="chi-siamo")
        tree.create_node("politica-per-la-qualita-di-ateneo", "politica-per-la-qualita-di-ateneo", parent="chi-siamo")
        tree.create_node("polimi-2040", "polimi-2040", parent="chi-siamo")
        tree.show()

        node = tree.get_node("polimi-2040")
        full_link = mappsite.helpers.link_cat(tree, node)
        self.assertEqual(full_link, "https://www.polimi.it/il-politecnico/chi-siamo/polimi-2040")


if __name__ == '__main__':
    unittest.main()
