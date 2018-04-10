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

#mean and variance from total population taken from mini-project1
totmean = [394.85785358919685, 436.9387900355872, 481.35394456289987, 346.88210227272725, 395.8528784648188, 362.01137980085343, 500.63985765124556, 368.4985754985755, 415.6159317211949, 
	469.16809116809117, 312.6635911994322, 384.03772241992885, 347.61603974449963, 351.64960909737033, 292.56472261735416, 304.40709219858155, 380.29545454545456, 440.8391459074733, 
	333.8417317246274, 348.16619318181813, 327.6557610241821, 337.8764204545455, 417.1511047754811, 527.5352313167259, 290.2874378992193, 474.7067615658363]
totvar = [22243.73388110721, 45632.44892237941, 39346.424829856114, 15085.540077398662, 24463.524197471357, 14342.68977092691, 54345.434710300004, 25932.9793427001, 24217.610670789058, 
	36607.109921997384, 7757.989029260862, 23242.585765631113, 17479.49132540937, 10837.394639150662, 3856.4022832445626, 7210.254134097893, 19362.61867252062, 54083.90010460862, 
	18006.932367760528, 9072.682607099065, 12595.649636085116, 17580.087000823158, 49638.273674830794, 45981.40178366541, 2666.227528495976, 45471.11401122072]
#calcuate stderror for questions
stderrall = np.zeros(num_qs)
for i in range(num_qs):
	stderrall[i] = math.sqrt(totvar[i]) / math.sqrt(p1countm[i]+p1countf[i] + p2countm[i]+p2countf[i] + p3countm[i]+p3countf[i] + p4countm[i]+p4countf[i] + p5countm[i]+p5countf[i])
print(stderrall)
meanmale = np.zeros(num_qs)
meanfemale = np.zeros(num_qs)
varmale = np.zeros(num_qs)
varfemale = np.zeros(num_qs)
malez = np.zeros(num_qs)
femalez = np.zeros(num_qs)
mstderr = np.zeros(num_qs)
fstderr = np.zeros(num_qs)
stderr = np.zeros(num_qs)
zs = np.zeros(num_qs)

for i in range(num_qs):
	meanmale[i] = p1countm[i]*p1qm[i] + p2countm[i]*p2qm[i] + p3countm[i]*p3qm[i] + p4countm[i]*p4qm[i] + p5countm[i]*p5qm[i]
	varmale[i] = (math.pow(p1countm[i],2)*p1qm[i] + math.pow(p2countm[i],2)*p2qm[i] + math.pow(p3countm[i],2)*p3qm[i] + math.pow(p4countm[i],2)*p4qm[i] + math.pow(p5countm[i],2)*p5qm[i]) - math.pow(meanmale[i],2)
	meanfemale[i] = p1countf[i]*p1qf[i] + p2countf[i]*p2qf[i] + p3countf[i]*p3qf[i] + p4countf[i]*p4qf[i] + p5countf[i]*p5qf[i]
	varfemale[i] = (math.pow(p1countf[i],2)*p1qf[i] + math.pow(p2countf[i],2)*p2qf[i] + math.pow(p3countf[i],2)*p3qf[i] + math.pow(p4countf[i],2)*p4qf[i] + math.pow(p5countf[i],2)*p5qf[i]) -math.pow(meanfemale[i],2)

	#malez[i] = (totmean[i] - meanmale[i]) / stderrall[i]
	#femalez[i] = (totmean[i] - meanfemale[i]) / stderrall[i]

	mstderr[i] = varmale[i] / (p1countm[i] + p2countm[i] + p3countm[i] + p4countm[i] + p5countm[i])
	fstderr[i] = varfemale[i] / (p1countf[i] + p2countf[i] + p3countf[i] + p4countf[i] + p5countf[i])	
	stderr[i] = math.sqrt(mstderr[i]+fstderr[i])
	zs[i] = (meanmale[i] - meanfemale[i]) / stderr[i]
print(zs)
print(meanmale)
print(meanfemale)
print(malez)
print(femalez)

	
