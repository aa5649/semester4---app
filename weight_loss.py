def weight_loss(N1,N2):
  max=0
  for i in range(1,len(N1)):
    if N1[i] - N2[i] >max:
      max = N1[i] - N2[i]
  print("Winner is friend",str(i+1))
  
 
N1 = list(map(int,input().split()))
N2 = list(map(int,input().split()))

weight_loss(N1,N2)
