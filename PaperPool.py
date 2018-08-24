class PaperPool:
   
    import matplotlib.pyplot as plt

    def Lcm(a,b):
        from fractions import gcd
        GCD=gcd(a,b)
        return(a*b)//GCD

    def getCount(Width, Height):
        WHLcm=Lcm(Width,Height)
        return (WHLcm/Height)+(WHLcm/Width)

    def getVal(Width,Height,lcd):
        Width=(lcd/Width)%2
        Height=(lcd/Height)%2
        if(Width==1 and Height==1 or Width==0 and Height==0):
            return 'C'
        if(Width==1 and Height==0):
            return 'D'
        if(Width==0 and Height==1):
            return 'B'



    dim=int(input("Please enter the dimensions you want to have: "))
    column_Width=list(range(1,dim+1))
    rows_Height=list(range(1,dim+1))

    data_list=[]

    for Width in range(1,dim+1):
        data_list.append([])
        for Height in range(1, dim+1):
            lcm=Lcm(Width,Height)
            data_list[Width-1].append((lcm/Width)+(lcm/Height))

    colorArray = []
    for i in range(1,dim + 1):
        colorArray.append([])
        for j in range(1,dim+1):
            lcd=Lcm(i,j)
            if (getVal(i, j, lcd) == 'B'):
                colorArray[i-1].append('r')
            if (getVal(i, j, lcd) == 'C'):
                colorArray[i-1].append('g')
            if (getVal(i, j,lcd) == 'D'):
                colorArray[i-1].append('b')



    ax=plt.subplot2grid((4,3),(0,0),colspan=3,rowspan=3)
    ax.table(cellText=data_list,rowLabels=rows_Height,colLabels=column_Width,loc='upper center',cellColours= colorArray)
    ax.axis("off")
    plt.title('Pool Poker')


    plt.show(ax)