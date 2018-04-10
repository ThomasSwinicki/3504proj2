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
bar_width = 0.35
ind = np.arange(5)
for i in range(num_qs):
	p1qm[i] = p1countm[i]/total_respm[i]
	p2qm[i] = p2countm[i]/total_respm[i]
	p3qm[i] = p3countm[i]/total_respm[i]
	p4qm[i] = p4countm[i]/total_respm[i]
	p5qm[i] = p5countm[i]/total_respm[i]
	pqm = [p1qm[i],p2qm[i],p3qm[i],p4qm[i],p5qm[i]]
	outm.write("Probabilities of male responses in Q" + str(i+1) + " : 1) "+ str(p1qm[i]) + " 2) "+  str(p2qm[i]) + " 3) "+  str(p3qm[i]) + " 4) " + str(p4qm[i]) + " 5) "+ str(p5qm[i]) + ".\n")
	plt.bar(ind,pqm,bar_width,color='red',label='Males')
	plt.title('Q' + str(i+1) +' distributions')# for males')
	plt.xlabel('Response')
	plt.ylabel('Probability')
	
	p1qf[i] = p1countf[i]/total_respf[i]
	p2qf[i] = p2countf[i]/total_respf[i]
	p3qf[i] = p3countf[i]/total_respf[i]
	p4qf[i] = p4countf[i]/total_respf[i]
	p5qf[i] = p5countf[i]/total_respf[i]
	pqf = [p1qf[i],p2qf[i],p3qf[i],p4qf[i],p5qf[i]]
	outf.write("Probabilities of female responses in Q" + str(i+1) + " : 1) "+ str(p1qf[i]) + " 2) "+  str(p2qf[i]) + " 3) "+  str(p3qf[i]) + " 4) " + str(p4qf[i]) + " 5) "+ str(p5qf[i]) + ".\n")
	plt.bar(ind+bar_width,pqf,bar_width, color='blue', label = 'Females')
	plt.legend()
	plt.savefig('Q' + str(i+1) +'distributions.png')
	plt.clf()

#compute the Hellinger distance between male and female for each question
#hellinger = np.zeros((num_qs, num_qs))
#hellinger[0,0] = 1
hellinger = np.zeros(num_qs)
hmin = 500
hmax = 0
hminquestion = 0
hmaxquestion = 0
#hellout = open('hellinger.txt','a')
for i in range(num_qs):
	hellinger[i] = ( (1/math.sqrt(2)) * math.sqrt( math.pow(  math.sqrt( p1qm[i]) - math.sqrt(p1qf[i]) , 2)
							+ math.pow(  math.sqrt( p2qm[i]) - math.sqrt(p2qf[i]) , 2)
							+ math.pow(  math.sqrt( p3qm[i]) - math.sqrt(p3qf[i]) , 2)
							+ math.pow(  math.sqrt( p4qm[i]) - math.sqrt(p4qf[i]) , 2)
							+ math.pow(  math.sqrt( p5qm[i]) - math.sqrt(p5qf[i]) , 2)))
	if(hellinger[i] > hmax):
		hmax = hellinger[i]
		hmaxquestion = i+1
	if(hellinger[i] < hmin):
		hmin = hellinger[i]
		hminquestion = i + 1
	#hellout.write('Question ' + str(i+1) + ' hellinger distance between male and females: ' + str(hellinger[i]) + '\n')
#print(hellinger)

meanmale = np.zeros(num_qs)
meanfemale = np.zeros(num_qs)
varmale = np.zeros(num_qs)
varfemale = np.zeros(num_qs)
mstderr = np.zeros(num_qs)
fstderr = np.zeros(num_qs)
stderr = np.zeros(num_qs)
zs = np.zeros(num_qs)

for i in range(num_qs):
	meanmale[i] = p1countm[i]*p1qm[i] + p2countm[i]*p2qm[i] + p3countm[i]*p3qm[i] + p4countm[i]*p4qm[i] + p5countm[i]*p5qm[i]
	varmale[i] = (math.pow(p1countm[i],2)*p1qm[i] + math.pow(p2countm[i],2)*p2qm[i] + math.pow(p3countm[i],2)*p3qm[i] + math.pow(p4countm[i],2)*p4qm[i] + math.pow(p5countm[i],2)*p5qm[i]) - math.pow(meanmale[i],2)
	meanfemale[i] = p1countf[i]*p1qf[i] + p2countf[i]*p2qf[i] + p3countf[i]*p3qf[i] + p4countf[i]*p4qf[i] + p5countf[i]*p5qf[i]
	varfemale[i] = (math.pow(p1countf[i],2)*p1qf[i] + math.pow(p2countf[i],2)*p2qf[i] + math.pow(p3countf[i],2)*p3qf[i] + math.pow(p4countf[i],2)*p4qf[i] + math.pow(p5countf[i],2)*p5qf[i]) -math.pow(meanfemale[i],2)

	mstderr[i] = varmale[i] / (total_respm[i])
	fstderr[i] = varfemale[i] / (total_respf[i]) 
	stderr[i] = math.sqrt((mstderr[i]+fstderr[i]))
	zs[i] = (meanmale[i] - meanfemale[i]) / stderr[i]
print(str(zs) + "Z scores\n")
print(str(meanmale) + "Male means\n")
print(str(meanfemale) + "Female means\n")
print(str(varmale) + "Male variances\n")
print(str(varfemale) + "Female variances\n")
