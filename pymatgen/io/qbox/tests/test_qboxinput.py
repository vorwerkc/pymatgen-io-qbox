import unittest
import numpy as np

from pymatgen.io.qbox import QboxInput
from pymatgen.util.testing import PymatgenTest

class QboxInputTest(unittest.TestCase):
    def test_write_str_with_oxidation(self):
        s = self.get_structure('Li2O')
        pseudos = {'O2-':'O_test.xml', 'Li+':'Li_test.xml'}
        qbox = QboxInput(s, pseudos= pseudos)
        ans = """set cell 5.513065396413618 0.18499354844278126 2.8723925155549113 1.8228941838858226 5.206262766491295 2.8723925155549113 0.251723519561044 0.18499366182634874 6.211374266082111 
species O2- O_test.xml
species Li+ Li_test.xml
atom O1 O2- 0.0 0.0 0.0 
atom Li2 Li+ 5.692115132915238 4.183181672178676 8.969251136535048 
atom Li3 Li+ 1.895567966945247 1.3930683045817498 2.986908160656887 
        """

        self.assertEqual(qbox.__str__(), ans)

    def test_read_str(unittest.Testcase):
        string = """set cell    20.52 0 0  0 20.52 0  0 0 20.52
species silicon Si_VBC_LDA-1.0.xml
atom Si01 silicon   -10.260000   -10.260000   -10.260000
atom Si02 silicon    -7.695000    -7.695000    -7.695000
atom Si03 silicon    -5.130000    -5.130000   -10.260000
atom Si04 silicon    -2.565000    -2.565000    -7.695000
atom Si05 silicon   -10.260000    -5.130000    -5.130000
atom Si06 silicon    -7.695000    -2.565000    -2.565000
atom Si07 silicon    -5.130000   -10.260000    -5.130000
atom Si08 silicon    -2.565000    -7.695000    -2.565000
atom Si09 silicon   -10.260000   -10.260000     0.000000
atom Si10 silicon    -7.695000    -7.695000     2.565000
atom Si11 silicon    -5.130000    -5.130000     0.000000
atom Si12 silicon    -2.565000    -2.565000     2.565000
atom Si13 silicon   -10.260000    -5.130000     5.130000
atom Si14 silicon    -7.695000    -2.565000     7.695000
atom Si15 silicon    -5.130000   -10.260000     5.130000
atom Si16 silicon    -2.565000    -7.695000     7.695000
atom Si17 silicon   -10.260000     0.000000   -10.260000
atom Si18 silicon    -7.695000     2.565000    -7.695000
atom Si19 silicon    -5.130000     5.130000   -10.260000
atom Si20 silicon    -2.565000     7.695000    -7.695000
atom Si21 silicon   -10.260000     5.130000    -5.130000
atom Si22 silicon    -7.695000     7.695000    -2.565000
atom Si23 silicon    -5.130000     0.000000    -5.130000
atom Si24 silicon    -2.565000     2.565000    -2.565000
atom Si25 silicon   -10.260000     0.000000     0.000000
atom Si26 silicon    -7.695000     2.565000     2.565000
atom Si27 silicon    -5.130000     5.130000     0.000000
atom Si28 silicon    -2.565000     7.695000     2.565000
atom Si29 silicon   -10.260000     5.130000     5.130000
atom Si30 silicon    -7.695000     7.695000     7.695000
atom Si31 silicon    -5.130000     0.000000     5.130000
atom Si32 silicon    -2.565000     2.565000     7.695000
atom Si33 silicon     0.000000   -10.260000   -10.260000
atom Si34 silicon     2.565000    -7.695000    -7.695000
atom Si35 silicon     5.130000    -5.130000   -10.260000
atom Si36 silicon     7.695000    -2.565000    -7.695000
atom Si37 silicon     0.000000    -5.130000    -5.130000
atom Si38 silicon     2.565000    -2.565000    -2.565000
atom Si39 silicon     5.130000   -10.260000    -5.130000
atom Si40 silicon     7.695000    -7.695000    -2.565000
atom Si41 silicon     0.000000   -10.260000     0.000000
atom Si42 silicon     2.565000    -7.695000     2.565000
atom Si43 silicon     5.130000    -5.130000     0.000000
atom Si44 silicon     7.695000    -2.565000     2.565000
atom Si45 silicon     0.000000    -5.130000     5.130000
atom Si46 silicon     2.565000    -2.565000     7.695000
atom Si47 silicon     5.130000   -10.260000     5.130000
atom Si48 silicon     7.695000    -7.695000     7.695000
atom Si49 silicon     0.000000     0.000000   -10.260000
atom Si50 silicon     2.565000     2.565000    -7.695000
atom Si51 silicon     5.130000     5.130000   -10.260000
atom Si52 silicon     7.695000     7.695000    -7.695000
atom Si53 silicon     0.000000     5.130000    -5.130000
atom Si54 silicon     2.565000     7.695000    -2.565000
atom Si55 silicon     5.130000     0.000000    -5.130000
atom Si56 silicon     7.695000     2.565000    -2.565000
atom Si57 silicon     0.000000     0.000000     0.000000
atom Si58 silicon     2.565000     2.565000     2.565000
atom Si59 silicon     5.130000     5.130000     0.000000
atom Si60 silicon     7.695000     7.695000     2.565000
atom Si61 silicon     0.000000     5.130000     5.130000
atom Si62 silicon     2.565000     7.695000     7.695000
atom Si63 silicon     5.130000     0.000000     5.130000
atom Si64 silicon     7.695000     2.565000     7.695000
        """
        lattice = np.array([10.858716, 0.000000, 0.000000],
                [0.000000, 10.858716, 0.000000],
                [0.000000, 0.000000, 10.858716])

        sites = np.array([
                [[-5.42935818, -5.42935818, -5.42935818],
                 [-4.07201864, -4.07201864, -4.07201864],
                 [-2.71467909, -2.71467909, -5.42935818],
                 [-1.35733955, -1.35733955, -4.07201864],
                 [-5.42935818, -2.71467909, -2.71467909],
                 [-4.07201864, -1.35733955, -1.35733955],
                 [-2.71467909, -5.42935818, -2.71467909],
                 [-1.35733955, -4.07201864, -1.35733955],
                 [-5.42935818, -5.42935818,  0.        ],
                 [-4.07201864, -4.07201864,  1.35733955],
                 [-2.71467909, -2.71467909,  0.        ],
                 [-1.35733955, -1.35733955,  1.35733955],
                 [-5.42935818, -2.71467909,  2.71467909],
                 [-4.07201864, -1.35733955,  4.07201864],
                 [-2.71467909, -5.42935818,  2.71467909],
                 [-1.35733955, -4.07201864,  4.07201864],
                 [-5.42935818,  0.        , -5.42935818],
                 [-4.07201864,  1.35733955, -4.07201864],
                 [-2.71467909,  2.71467909, -5.42935818],
                 [-1.35733955,  4.07201864, -4.07201864],
                 [-5.42935818,  2.71467909, -2.71467909],
                 [-4.07201864,  4.07201864, -1.35733955],
                 [-2.71467909,  0.        , -2.71467909],
                 [-1.35733955,  1.35733955, -1.35733955],
                 [-5.42935818,  0.        ,  0.        ],
                 [-4.07201864,  1.35733955,  1.35733955],
                 [-2.71467909,  2.71467909,  0.        ],
                 [-1.35733955,  4.07201864,  1.35733955],
                 [-5.42935818,  2.71467909,  2.71467909],
                 [-4.07201864,  4.07201864,  4.07201864],
                 [-2.71467909,  0.        ,  2.71467909],
                 [-1.35733955,  1.35733955,  4.07201864],
                 [ 0.        , -5.42935818, -5.42935818],
                 [ 1.35733955, -4.07201864, -4.07201864],
                 [ 2.71467909, -2.71467909, -5.42935818],
                 [ 4.07201864, -1.35733955, -4.07201864],
                 [ 0.        , -2.71467909, -2.71467909],
                 [ 1.35733955, -1.35733955, -1.35733955],
                 [ 2.71467909, -5.42935818, -2.71467909],
                 [ 4.07201864, -4.07201864, -1.35733955],
                 [ 0.        , -5.42935818,  0.        ],
                 [ 1.35733955, -4.07201864,  1.35733955],
                 [ 2.71467909, -2.71467909,  0.        ],
                 [ 4.07201864, -1.35733955,  1.35733955],
                 [ 0.        , -2.71467909,  2.71467909],
                 [ 1.35733955, -1.35733955,  4.07201864],
                 [ 2.71467909, -5.42935818,  2.71467909],
                 [ 4.07201864, -4.07201864,  4.07201864],
                 [ 0.        ,  0.        , -5.42935818],
                 [ 1.35733955,  1.35733955, -4.07201864],
                 [ 2.71467909,  2.71467909, -5.42935818],
                 [ 4.07201864,  4.07201864, -4.07201864],
                 [ 0.        ,  2.71467909, -2.71467909],
                 [ 1.35733955,  4.07201864, -1.35733955],
                 [ 2.71467909,  0.        , -2.71467909],
                 [ 4.07201864,  1.35733955, -1.35733955],
                 [ 0.        ,  0.        ,  0.        ],
                 [ 1.35733955,  1.35733955,  1.35733955],
                 [ 2.71467909,  2.71467909,  0.        ],
                 [ 4.07201864,  4.07201864,  1.35733955],
                 [ 0.        ,  2.71467909,  2.71467909],
                 [ 1.35733955,  4.07201864,  4.07201864],
                 [ 2.71467909,  0.        ,  2.71467909],
                 [ 4.07201864,  1.35733955,  4.07201864]]
            ])

            qbox = QboxInput.from_string(string)

            # generate array of site coordinates
            qbox_sites = []
            for site in qbox.structure.sites:
                qbox_sites.append(list(site.coords))
            qbox_sites = np.array(qbox_sites)

            np.testing.assert_allclose(sites, qbox_sites)

            np.testing.assert_allclose(lattice, qbox.structure.lattice.matrix)
