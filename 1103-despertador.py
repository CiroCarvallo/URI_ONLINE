while True:
    h1, m1, h2 , m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
      break
    else:
      A = h1*60 + m1
      B = h2*60 + m2
      
      if(B <= A):
        B += 24*60
      
      print(abs(B-A))
