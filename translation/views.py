from django.shortcuts import render
from django.views.generic.base import View, HttpResponseRedirect

class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = request.POST
        inputText = form.get('inputtext')
        textbreak = inputText.split()
        # print(form)
        # print(inputText)
        # print(textbreak)

        codon = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
	            "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
	            "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
	            "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 
	            "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
	            "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
	            "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
	            "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 
	            "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
	            "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
	            "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
	            "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 
	            "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
	            "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
	            "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
	            "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

        sequence_name = list()
        protein_sequence = list()
        tmp = ""
        sequence_line = ""
        seq_num = 1
        for line in textbreak:
            if line.startswith(">"):
                line = line.replace(line,"sequence"+str(seq_num))
                sequence_name.append(line)
                seq_num += 1
                if not tmp:
                    continue
                else:
                    for i in range(0,len(tmp)-((3+len(tmp))%3),3):
                        sequence_line += codon[tmp[i:i+3]]
                    sequence_line = list(sequence_line)
                    chr_position = 70
                    for chr in range(len(sequence_line)):
                        if chr == chr_position:
                            sequence_line.insert(chr_position,"<br>")
                            chr_position += 70
                        else:
                            continue
                    sequence_line = ''.join(sequence_line)
                    protein_sequence.append(sequence_line)
                    tmp = ""
                    sequence_line = ""
            else:
                line = line.upper()
                line = line.replace("T","U")
                tmp += line

        for i in range(0,len(tmp)-((3+len(tmp))%3),3):
            sequence_line += codon[tmp[i:i+3]]
        sequence_line = list(sequence_line)
        chr_position = 70
        for chr in range(len(sequence_line)):
            if chr == chr_position:
                sequence_line.insert(chr_position,"<br>")
                chr_position += 70
            else:
                continue
        sequence_line = ''.join(sequence_line)
        protein_sequence.append(sequence_line)

        resultA = list()
        resultC = list()
        resultD = list()
        resultE = list()
        resultF = list()
        resultG = list()
        resultH = list()
        resultI = list()
        resultK = list()
        resultL = list()
        resultM = list()
        resultN = list()
        resultP = list()
        resultQ = list()
        resultR = list()
        resultS = list()
        resultT = list()
        resultV = list()
        resultW = list()
        resultY = list()
        resultSTOP = list()
        resultSUM = list()
        for i in protein_sequence:
            ala = i.count("A")
            resultA.append(ala)
            cys = i.count("C")
            resultC.append(cys)
            asp = i.count("D")
            resultD.append(asp)
            glu = i.count("E")
            resultE.append(glu)
            phe = i.count("F")
            resultF.append(phe)
            gly = i.count("G")
            resultG.append(gly)
            his = i.count("H")
            resultH.append(his)
            ile = i.count("I")
            resultI.append(ile)
            lys = i.count("K")
            resultK.append(lys)
            leu = i.count("L")
            resultL.append(leu)
            met = i.count("M")
            resultM.append(met)
            asn = i.count("N")
            resultN.append(asn)
            pro = i.count("P")
            resultP.append(pro)
            gln = i.count("Q")
            resultQ.append(gln)
            arg = i.count("R")
            resultR.append(arg)
            ser = i.count("S")
            resultS.append(ser)
            thr = i.count("T")
            resultT.append(thr)
            val = i.count("V")
            resultV.append(val)
            trp = i.count("W")
            resultW.append(trp)
            tyr = i.count("Y")
            resultY.append(tyr)
            stop = i.count("_")
            resultSTOP.append(stop)
            total = len(i)
            resultSUM.append(total)

        insert_results = zip(sequence_name,resultA,resultC,resultD,resultE,
            resultF,resultG,resultH,resultI,resultK,resultL,resultM,
            resultN,resultP,resultQ,resultR,resultS,resultT,resultV,
            resultW,resultY,resultSTOP,resultSUM)

        concat_lists = zip(sequence_name, protein_sequence, resultSUM)
        print(list(insert_results))
        print(list(concat_lists))