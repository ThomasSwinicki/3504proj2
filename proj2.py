import numpy as np
import xlrd
import pandas
import math
import matplotlib.pyplot as plt


#open excel file in variable answers
answers = pandas.read_excel('mini-project2-data-v3.xlsx')

print(answers.columns)
print(answers.columns[26])

num_qs = len(answers.columns) - 1

#column index 26 is gender
#array of probabilities of each response for each question for males where index is question nunmber-1
p1qm = np.zeros(num_qs)
p2qm = np.zeros(num_qs)
p3qm = np.zeros(num_qs)
p4qm = np.zeros(num_qs)
p5qm = np.zeros(num_qs)

#total responses (excluding 0s) for each question for males where index is question number-1
total_respm = np.zeros(num_qs)

#array of counts for each response for males where index is question number-1
p1countm = np.zeros(num_qs)
p2countm = np.zeros(num_qs)
p3countm = np.zeros(num_qs)
p4countm = np.zeros(num_qs)
p5countm = np.zeros(num_qs)

#array of probabilities of each response for each question for females where index is question nunmber-1
p1qf = np.zeros(num_qs)
p2qf = np.zeros(num_qs)
p3qf = np.zeros(num_qs)
p4qf = np.zeros(num_qs)
p5qf = np.zeros(num_qs)

#total responses (excluding 0s) for each question for females where index is question number-1
total_respf = np.zeros(num_qs)

#array of counts for each response for females where index is question number-1
p1countf = np.zeros(num_qs)
p2countf = np.zeros(num_qs)
p3countf = np.zeros(num_qs)
p4countf = np.zeros(num_qs)
p5countf = np.zeros(num_qs)

for i in range(num_qs):
	for n in range(len(answers['Q1'].values)):
		if(answers['Q'+str(i+1)].values[n] == 1 and answers['gender'].values[n] == 2):
			p1countm[i] += 1
			total_respm[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 2 and answers['gender'].values[n] == 2):
                        p2countm[i] += 1
                        total_respm[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 3 and answers['gender'].values[n] == 2):
                        p3countm[i] += 1
                        total_respm[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 4 and answers['gender'].values[n] == 2):
                        p4countm[i] += 1
                        total_respm[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 5 and answers['gender'].values[n] == 2):
                        p5countm[i] += 1
                        total_respm[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 1 and answers['gender'].values[n] == 1):
			p1countf[i] += 1
			total_respf[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 2 and answers['gender'].values[n] == 1):
                        p2countf[i] += 1
                        total_respf[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 3 and answers['gender'].values[n] == 1):
                        p3countf[i] += 1
                        total_respf[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 4 and answers['gender'].values[n] == 1):
                        p4countf[i] += 1
                        total_respf[i] += 1
		elif(answers['Q'+str(i+1)].values[n] == 5 and answers['gender'].values[n] == 1):
                        p5countf[i] += 1
                        total_respf[i] += 1

outm = open('maledistros.txt', 'w');
outf = open('femaledistros.txt', 'w');
for i in range(num_qs):
	p1qm[i] = p1countm[i]/total_respm[i]
	p2qm[i] = p2countm[i]/total_respm[i]
	p3qm[i] = p3countm[i]/total_respm[i]
	p4qm[i] = p4countm[i]/total_respm[i]
	p5qm[i] = p5countm[i]/total_respm[i]
	#with open('maledistros.txt','a') as out:
	#	out.write("Probabilities of male responses in Q" + str(i+1) + " : 1) "+ str(p1qm[i]) + " 2) "+  str(p2qm[i]) + " 3) "+  str(p3qm[i]) + " 4) " + str(p4qm[i]) + " 5) "+ str(p5qm[i]) + ".\n")
	outm.write("Probabilities of male responses in Q" + str(i+1) + " : 1) "+ str(p1qm[i]) + " 2) "+  str(p2qm[i]) + " 3) "+  str(p3qm[i]) + " 4) " + str(p4qm[i]) + " 5) "+ str(p5qm[i]) + ".\n")
	plt.bar(1,p1qm[i],color='red')
	plt.bar(2,p2qm[i],color='purple')
	plt.bar(3,p3qm[i],color='blue')
	plt.bar(4,p4qm[i],color='green')
	plt.bar(5,p5qm[i],color='orange')
	plt.title('Q' + str(i+1) +' distribution for males')
	plt.xlabel('Response')
	plt.ylabel('Probability')
	plt.savefig('Q' + str(i+1) +'maledistribution.png')
	plt.clf()
	
	p1qf[i] = p1countf[i]/total_respf[i]
	p2qf[i] = p2countf[i]/total_respf[i]
	p3qf[i] = p3countf[i]/total_respf[i]
	p4qf[i] = p4countf[i]/total_respf[i]
	p5qf[i] = p5countf[i]/total_respf[i]
	#with open('distros.txt','a') as out:
	#	out.write("Probabilities of female responses in Q" + str(i+1) + " : 1) "+ str(p1qf[i]) + " 2) "+  str(p2qf[i]) + " 3) "+  str(p3qf[i]) + " 4) " + str(p4qf[i]) + " 5) "+ str(p5qf[i]) + ".\n")
	outf.write("Probabilities of female responses in Q" + str(i+1) + " : 1) "+ str(p1qf[i]) + " 2) "+  str(p2qf[i]) + " 3) "+  str(p3qf[i]) + " 4) " + str(p4qf[i]) + " 5) "+ str(p5qf[i]) + ".\n")
	plt.bar(1,p1qf[i],color='red')
	plt.bar(2,p2qf[i],color='purple')
	plt.bar(3,p3qf[i],color='blue')
	plt.bar(4,p4qf[i],color='green')
	plt.bar(5,p5qf[i],color='orange')
	plt.title('Q' + str(i+1) +' distribution for females')
	plt.xlabel('Response')
	plt.ylabel('Probability')
	plt.savefig('Q' + str(i+1) +'femaledistribution.png')
	plt.clf()

