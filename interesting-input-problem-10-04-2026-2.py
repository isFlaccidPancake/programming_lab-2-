#we count stream from left to right, from 1 to 100 streams. they split and rejoin.
#every time te number changes, we renumber them assgning the number from left to right
strams_at_high_altitude= int(input())   #the following inputs tell how much water flow in each stream
                                        # from left to right(first input() most left )
#99 means a split has happened: tell which stream splitted and how much water flows in the left one( right= total-left)
#88 means a joint happened: a stream number N joins to the one on its right (N+1)
#77 to finish the algorithm, and print the flow in each stream
streams_flow=[]
string=''
for i in range(0, strams_at_high_altitude):
    streams_flow.append(int(input()))
boolean=True
while boolean:
    mode=input()
    if mode=='77':
        for j in range(0,len(streams_flow)):
            if j==(len(streams_flow)-1):
                 string+=str(round(streams_flow[j]))
            else:

                string+=str(round(streams_flow[j]))+' '

        print( string)
        boolean=False

    elif mode=='99':
        stream_index=int(input())-1
        flow_percentage_left= int(input())
        flow_percentage_right= 100-flow_percentage_left
        value= streams_flow[stream_index]
        streams_flow[stream_index]= value*(flow_percentage_left/100)
        new_stream= value-streams_flow[stream_index]
        streams_flow.insert(stream_index+1, new_stream )

    elif mode=='88':
        stream_index=int(input())-1
        value= streams_flow[stream_index]
        streams_flow.pop(stream_index)
        streams_flow[stream_index]+=value

