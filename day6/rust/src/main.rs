fn first_task(datastream_buffer: Vec<u8>) {
    let mut left = 0;
    let mut right = 3;
    let mut finished = false;
    while !finished {
        finished = true;
        for i in left..right {
            for j in ((i + 1)..=right).rev() {
                if datastream_buffer[i] == datastream_buffer[j] {
                    left = i + 1;
                    right = i + 4;
                    finished = false;
                    break;
                }
            }
            if !finished {
                break;
            }
        }
    }
    println!("first task: {}", right + 1);
}

fn second_task(datastream_buffer: Vec<u8>) {
    let mut left = 0;
    let mut right = 13;
    let mut finished = false;
    while !finished {
        finished = true;
        for i in left..right {
            for j in ((i + 1)..=right).rev() {
                if datastream_buffer[i] == datastream_buffer[j] {
                    left = i + 1;
                    right = i + 14;
                    finished = false;
                    break;
                }
            }
            if !finished {
                break;
            }
        }
    }
    println!("second task: {}", right + 1);
}

fn main() {
    let datastream_buffer = "dfsfmfbbbjnbbpddfcfjcjbjwjqqbtbntnhtnncfnfpnffwpphwppvbvtvztzszfzhhnqnvnpppmzmczcmzczbznnbssbhhvghhzqzvzttjvtvcccdhccmvccgdgttghthppwlwqlwwcswspsfsdfddhwwzlwzwttlglttsjjthhgcgfcfhfhtftrffwcfcsfccnntmmpvpgpfgfsgfflgfgmffbmmqsmqmmcqqmjjzczwczzpjzzgtgnnqqvdqvqllbttftgtztcztttlslrslrlfldljlwjjnvjjmrrhdrhhflhffgnfnjffmvmvjjspsvvrcchhgngwwdwbwwfhwffmggbsgspsjsfjjdwwbtbdtbdbgdbbbzhzvhhwpwlwfwfswwrgggmggssfwwdrwrccssjttltrrnggdbggvzzzrfzfwzfffnfnmnnzmnznpzzdtzdttbvvgffmnfmfmbbqppcgpgtgpgggcwwlpplslbslblhlmlfmlmldmmjhjjgllglhlssswcssprrqrjrhrvrffpfnpfnppzgztgtdgtdggftgftggqrgrnnqpnpgnpnggsjsvscsnswshwswfwfwqffcrrmprrrcgrrggmnnmzmwzmwzzgzzhnzzthtggtmmdrmrbmmqwwjswwphhzvvjqjrrvzrrmssdvdlvvlhvvjggbwbrwwjqjqmmfllttvpttdvtdtddrttpltpllzrlrwlrrvcvpcphcccqwwtpwwbmmtntfntftvfvfqvvwnvwwvhhlccvrcrlclcqcvqqsvvfjjqmmfhfvvctczzlhlsslpspfsswnsnzsspzpccmssmpmbpbmmvnvsnvsszttrppvgpgnncllrvlrvllcvlvwvhvghgvvnhvvmffclfccvwcvccrwrhhrffqrqcrqqhbqhqssmzsmzsmmzrztzllmclmmbgmbbrmrgrwrgwrrgngvvtqqpbqpppgbgccsjjcmmtdmdjmmjcchvchhbccnjngjjnwjnnrvnrrsqshshszzqnngbnnrnggvwwlzwwlqwqmqdqrdqqrhqhffpgffqgqdggfjgglfglgvgjvjmjtthghrhvhgvhvnncnwcnwntwntnjjqjwwrdwddsggfddnhnsnvsstbbjddfhddhbddwbwbnbrnnrhrqhqdhdllvbbnzzbmbttpjjngnqqcffrsrnsnnhzzgllgvlvcchfhzzmzrmrggdvgvgqqwnqqpdqqvjjvnvhnhhgvhhgllhlzlclbcccwppztzhhvmvzzzsbzbppvdvdtdtdvdsdlsscnnqhnhgngghrrzprzzpddmvvhcvvprplpnlppscctzthtptspttmftmftfjjdfdjfjrfrfbfcchmhnnbddwzwvvpvrvnnslnlnhlnhlltslttqpqvvgzvzsstcstsrtrbtbbzmmzrzqrzqqnmqnnpjpttwgtgzgqqgmgnnzgzrggpbggvssqvssmhmshmssvlvlmvvnhnhddwbbllffgbffbbztthbhdhdghhrccfmfrfmmbdbfdbffzfgfrfqqptpgpjjlvvbjjdzdbbszslzlldnngwgddbmbpbwwhphnhmhhlthhgfhfvvpmvmhvmvdvsddsjtzvfmpsrwrrzgcvnnllfjmvfptwncppfmgqbfzrdpnfddghsqfmnqfwfslrsgjmqtfqwhdddsbhtbtpswcbfppcbhzfzbsqljzndcsrlhrrtstgfhhfsqqrwgnncsmstdmjvfjhqnrczlftzzzhqdzjdcdqcgfpmbqntdhzcvbtpssrvmgjwzwfvtpsrsrwrvrsjgrmzqzvbttscldsnnwzvmlztnnpdjrwvhshpdwgvhmlrnhtfccjnldlnhtfncfjjjztjmhrdqpvhggtqzwjsvwdzhdmwhsmgzjcwzqzlwbrlzsmlwhpjvflnppvrbgrsblmjpnqvgpjbpwbjgjqzwvjbgcplccjgbfwlblzfjqpwszbqbcnlbmfmqpmgspscgfdgfwnmcdzcqnjznndjcvlblszcnpflbjqltpfzhffdbwbshtpnwwlspltpcrvbdtflwbjrfnvrflqpgqtjzqwmmsdvtsmgjtrtbrzchwhpfsznjqcbrjcvwqgrcsqpvfzhrdlmnvvhjzpgpnlrmqfvcnlrlcfjblfcgvngdjfdczsrtnnwjndsfcsdlhdnbtplfnhsmmbldmsjwcblghhgqwbnjvqbqhddrmrtncvwnchsfpddzgrrtzntmwnmdwlrvnjgnzjqvptztnqnqmcjmmrhmtstgdvhffbbmphnbtsdmpmscsfdbnfnchrhhjpsfhhswfszgqfcbdbgnrqhrflpfgfgdcrjvrwbvsfmzzhvzvqzgshcqzlfcljnlgshdlhwdchhhvwlshwdrgjfbnptqqglbpcfgrmqjhqvlbzdwgnzfzlpcpjzqwhbfjljszvjdsrmfzntgnjflhnwhpfrlbpvgzmbqwzlgphmbvbfdqfgqqbhzzvrjftnwjzhlrqccwcfzvntscnbfcsrqqnvlvhszpgwtrzjrqbtslctbhtbczwtmsgwczncbjmzqvnthpwjmsbsjnfpsmghnvtqjjnjfwtnmlthrlcpqhjpnvnbbnwrdjfshwhpdwmsbngfhbhsqphlqspcgzwrgfjmqqtlsfgnvqtdgnhmdvvqzjwlhsnvjczbssrnlhwdmdthmtprjjfttfzbbswfwsvvslfnbcvprzhtcqwdrzjrnjjctqfsjrsddlhzcnstqfppjlqhvcbjbfwndwdtdfvnlwgvdvhzzrqthdhdmddfdwschmpwwrnlgsldzhgjrlmtzrnrrtqfctvbncpcjlsvnwjvhgnbshhwlqhtjghvrctlvngjgjrlgshhwscrdvzjqtfrrbssvqlcjjdljpmlzfqqnqmffpsbvgcqzqdjwczbqwjgfvpdgjglnqdshppcsqcmszhrbcpnhjnczlhwsbnfnzsczjvmftngqcvhgpgwlzbmjnmmdvdjfrcwnjrncvfstrvvqsstphmqdpwjqhzgppmgwlgjhgfwqgmjrlsvqpfqznvbqzgtngvpbpttzvngjwtrjgdnvdggzlnmpgbzhtnfnrhgwvhnpqdwfdvvftzllpqblgdglclwtwbchlvwcmmvtchlntlghztfvgfjczcbqmzgnqmrjcmqvjmjhfpztjcvclblmrctzfmsdfvfpwdcbsglgrsjqcgtcblhbtgcgjlwhhqnwhdnwzlhvphtvmlfnbfmgpnnbzqtdtzqrbhfljlwstlbscnrsvhrbrcthvzcngrttddcjqhtmsfpsgldgtsgjtprsttlssmrrfjmrddqvnqcfmphbnjtdsqvptrdzqbqfjqtnrqtjgdpbrlzrlvwcbcqbcmncfmwcpdhgpjdrdcmrqnflsqbllrqslmhsljwghnwcjwvhchcnlgppmphbqtcdfzjpcqcgsjzvmgfjgfsvmvjfqvtpffbpmhnnnrjmqhhhrhrqfqdwzdvzssslzvqhngdpszztgrvjntcpzhbfmhbpvcndsjbtnwgpmztpbrtjmfqrsvndrspdqmlsbldgghfflncszhnsttfslvwhvfnsmmhbbvjqslsjfqplndndwmbmvgchgvhzclrcnhvgbgmpctrggvqpvqvgvncmdwhpmwhzwhlgsnlnwggfbbvdvqrrsmhwzrrpgrjfshzgzjpfwjhpqmqhbjlwhwsfszlshpzprvgprlprrvlcrmbttjrpqsrdcdfwdrzbcfjpvrlrjjdwhbspqmrblvtldqdhtjtjphpqswgvqfftdgqrtjgsmthlhvlcqrwlqtthwjgrcpwcnsqtssqzpzqptrwjjdfchfmmsrsccnlvqbdmbcdjmhpgvnnlttfhggfphvbwqtcztbnsflztcfpbcpjbcmsplhjdbsmzhgnmfrhscmwmfqbljvhgllvvgqzphzbswdzlhmpcvnntczrcnqvlphhjdjjjnhfzzcjjsdlfccwvswvjfgvmlnpvjvcbpglsgtpj";
    first_task(datastream_buffer.into());
    second_task(datastream_buffer.into());
}
