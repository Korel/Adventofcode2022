def first_task(datastream_buffer):
    left = 0
    right = 13
    finished = False
    while not finished:
        finished = True
        for i in range(left, right):
            for j in range(right, i, -1):
                if datastream_buffer[i] == datastream_buffer[j]:
                    left = i + 1
                    right = i + 4
                    finished = False
                    break
            if not finished:
                break
    
    print("first task:", right + 1)

def second_task(datastream_buffer):
    left = 0
    right = 13
    finished = False
    while not finished:
        finished = True
        for i in range(left, right):
            for j in range(right, i, -1):
                if datastream_buffer[i] == datastream_buffer[j]:
                    left = i + 1
                    right = i + 14
                    finished = False
                    break
            if not finished:
                break
    
    print("second task:", right + 1)


def main():
    datastream_buffer = "dfsfmfbbbjnbbpddfcfjcjbjwjqqbtbntnhtnncfnfpnffwpphwppvbvtvztzszfzhhnqnvnpppmzmczcmzczbznnbssbhhvghhzqzvzttjvtvcccdhccmvccgdgttghthppwlwqlwwcswspsfsdfddhwwzlwzwttlglttsjjthhgcgfcfhfhtftrffwcfcsfccnntmmpvpgpfgfsgfflgfgmffbmmqsmqmmcqqmjjzczwczzpjzzgtgnnqqvdqvqllbttftgtztcztttlslrslrlfldljlwjjnvjjmrrhdrhhflhffgnfnjffmvmvjjspsvvrcchhgngwwdwbwwfhwffmggbsgspsjsfjjdwwbtbdtbdbgdbbbzhzvhhwpwlwfwfswwrgggmggssfwwdrwrccssjttltrrnggdbggvzzzrfzfwzfffnfnmnnzmnznpzzdtzdttbvvgffmnfmfmbbqppcgpgtgpgggcwwlpplslbslblhlmlfmlmldmmjhjjgllglhlssswcssprrqrjrhrvrffpfnpfnppzgztgtdgtdggftgftggqrgrnnqpnpgnpnggsjsvscsnswshwswfwfwqffcrrmprrrcgrrggmnnmzmwzmwzzgzzhnzzthtggtmmdrmrbmmqwwjswwphhzvvjqjrrvzrrmssdvdlvvlhvvjggbwbrwwjqjqmmfllttvpttdvtdtddrttpltpllzrlrwlrrvcvpcphcccqwwtpwwbmmtntfntftvfvfqvvwnvwwvhhlccvrcrlclcqcvqqsvvfjjqmmfhfvvctczzlhlsslpspfsswnsnzsspzpccmssmpmbpbmmvnvsnvsszttrppvgpgnncllrvlrvllcvlvwvhvghgvvnhvvmffclfccvwcvccrwrhhrffqrqcrqqhbqhqssmzsmzsmmzrztzllmclmmbgmbbrmrgrwrgwrrgngvvtqqpbqpppgbgccsjjcmmtdmdjmmjcchvchhbccnjngjjnwjnnrvnrrsqshshszzqnngbnnrnggvwwlzwwlqwqmqdqrdqqrhqhffpgffqgqdggfjgglfglgvgjvjmjtthghrhvhgvhvnncnwcnwntwntnjjqjwwrdwddsggfddnhnsnvsstbbjddfhddhbddwbwbnbrnnrhrqhqdhdllvbbnzzbmbttpjjngnqqcffrsrnsnnhzzgllgvlvcchfhzzmzrmrggdvgvgqqwnqqpdqqvjjvnvhnhhgvhhgllhlzlclbcccwppztzhhvmvzzzsbzbppvdvdtdtdvdsdlsscnnqhnhgngghrrzprzzpddmvvhcvvprplpnlppscctzthtptspttmftmftfjjdfdjfjrfrfbfcchmhnnbddwzwvvpvrvnnslnlnhlnhlltslttqpqvvgzvzsstcstsrtrbtbbzmmzrzqrzqqnmqnnpjpttwgtgzgqqgmgnnzgzrggpbggvssqvssmhmshmssvlvlmvvnhnhddwbbllffgbffbbztthbhdhdghhrccfmfrfmmbdbfdbffzfgfrfqqptpgpjjlvvbjjdzdbbszslzlldnngwgddbmbpbwwhphnhmhhlthhgfhfvvpmvmhvmvdvsddsjtzvfmpsrwrrzgcvnnllfjmvfptwncppfmgqbfzrdpnfddghsqfmnqfwfslrsgjmqtfqwhdddsbhtbtpswcbfppcbhzfzbsqljzndcsrlhrrtstgfhhfsqqrwgnncsmstdmjvfjhqnrczlftzzzhqdzjdcdqcgfpmbqntdhzcvbtpssrvmgjwzwfvtpsrsrwrvrsjgrmzqzvbttscldsnnwzvmlztnnpdjrwvhshpdwgvhmlrnhtfccjnldlnhtfncfjjjztjmhrdqpvhggtqzwjsvwdzhdmwhsmgzjcwzqzlwbrlzsmlwhpjvflnppvrbgrsblmjpnqvgpjbpwbjgjqzwvjbgcplccjgbfwlblzfjqpwszbqbcnlbmfmqpmgspscgfdgfwnmcdzcqnjznndjcvlblszcnpflbjqltpfzhffdbwbshtpnwwlspltpcrvbdtflwbjrfnvrflqpgqtjzqwmmsdvtsmgjtrtbrzchwhpfsznjqcbrjcvwqgrcsqpvfzhrdlmnvvhjzpgpnlrmqfvcnlrlcfjblfcgvngdjfdczsrtnnwjndsfcsdlhdnbtplfnhsmmbldmsjwcblghhgqwbnjvqbqhddrmrtncvwnchsfpddzgrrtzntmwnmdwlrvnjgnzjqvptztnqnqmcjmmrhmtstgdvhffbbmphnbtsdmpmscsfdbnfnchrhhjpsfhhswfszgqfcbdbgnrqhrflpfgfgdcrjvrwbvsfmzzhvzvqzgshcqzlfcljnlgshdlhwdchhhvwlshwdrgjfbnptqqglbpcfgrmqjhqvlbzdwgnzfzlpcpjzqwhbfjljszvjdsrmfzntgnjflhnwhpfrlbpvgzmbqwzlgphmbvbfdqfgqqbhzzvrjftnwjzhlrqccwcfzvntscnbfcsrqqnvlvhszpgwtrzjrqbtslctbhtbczwtmsgwczncbjmzqvnthpwjmsbsjnfpsmghnvtqjjnjfwtnmlthrlcpqhjpnvnbbnwrdjfshwhpdwmsbngfhbhsqphlqspcgzwrgfjmqqtlsfgnvqtdgnhmdvvqzjwlhsnvjczbssrnlhwdmdthmtprjjfttfzbbswfwsvvslfnbcvprzhtcqwdrzjrnjjctqfsjrsddlhzcnstqfppjlqhvcbjbfwndwdtdfvnlwgvdvhzzrqthdhdmddfdwschmpwwrnlgsldzhgjrlmtzrnrrtqfctvbncpcjlsvnwjvhgnbshhwlqhtjghvrctlvngjgjrlgshhwscrdvzjqtfrrbssvqlcjjdljpmlzfqqnqmffpsbvgcqzqdjwczbqwjgfvpdgjglnqdshppcsqcmszhrbcpnhjnczlhwsbnfnzsczjvmftngqcvhgpgwlzbmjnmmdvdjfrcwnjrncvfstrvvqsstphmqdpwjqhzgppmgwlgjhgfwqgmjrlsvqpfqznvbqzgtngvpbpttzvngjwtrjgdnvdggzlnmpgbzhtnfnrhgwvhnpqdwfdvvftzllpqblgdglclwtwbchlvwcmmvtchlntlghztfvgfjczcbqmzgnqmrjcmqvjmjhfpztjcvclblmrctzfmsdfvfpwdcbsglgrsjqcgtcblhbtgcgjlwhhqnwhdnwzlhvphtvmlfnbfmgpnnbzqtdtzqrbhfljlwstlbscnrsvhrbrcthvzcngrttddcjqhtmsfpsgldgtsgjtprsttlssmrrfjmrddqvnqcfmphbnjtdsqvptrdzqbqfjqtnrqtjgdpbrlzrlvwcbcqbcmncfmwcpdhgpjdrdcmrqnflsqbllrqslmhsljwghnwcjwvhchcnlgppmphbqtcdfzjpcqcgsjzvmgfjgfsvmvjfqvtpffbpmhnnnrjmqhhhrhrqfqdwzdvzssslzvqhngdpszztgrvjntcpzhbfmhbpvcndsjbtnwgpmztpbrtjmfqrsvndrspdqmlsbldgghfflncszhnsttfslvwhvfnsmmhbbvjqslsjfqplndndwmbmvgchgvhzclrcnhvgbgmpctrggvqpvqvgvncmdwhpmwhzwhlgsnlnwggfbbvdvqrrsmhwzrrpgrjfshzgzjpfwjhpqmqhbjlwhwsfszlshpzprvgprlprrvlcrmbttjrpqsrdcdfwdrzbcfjpvrlrjjdwhbspqmrblvtldqdhtjtjphpqswgvqfftdgqrtjgsmthlhvlcqrwlqtthwjgrcpwcnsqtssqzpzqptrwjjdfchfmmsrsccnlvqbdmbcdjmhpgvnnlttfhggfphvbwqtcztbnsflztcfpbcpjbcmsplhjdbsmzhgnmfrhscmwmfqbljvhgllvvgqzphzbswdzlhmpcvnntczrcnqvlphhjdjjjnhfzzcjjsdlfccwvswvjfgvmlnpvjvcbpglsgtpj"
    first_task(datastream_buffer)
    second_task(datastream_buffer)

if __name__ == "__main__":
    main()

