## Summary 1-12 
TCP is a way for two computers to comunicate over a network. The first thing that happens is a handshake. Then packet transmission is started. The window size depends on packadge loss, buffer size at the reciver and sender aswell as congestion avoidance. Transmission starts with slow start and after a threshold it increases linearly. It increases untill buffersizes are met or untill packadge loss accurs.

RTT determines how fast we can send more packadges. High RTT means that we ahve to wait a long time to send new packadges since we might fill upp the reciver bufffer if we send them to quickly even if we have a high windows size and low congestion. If the RTT becomes longer than our timout for packadge loss we will start sending packadges again while engadging congestion avoidance. Congestion avoidance can be done in several ways, where the easiest way is to just start over with a slow start. 

It should be noted that in this trace file we stop increasing the window after 6 packadges. Even though the reciver buffer size increases, this is not the behavior we would expect, but since we don't know the algorithm used for the case predicti ons of that kind are hard to make,

6E8
4.5E8
8.7E8
6E8
2.3E8
2.3E8
8.2E8
8.1E8
3.9E8
3.4E8





