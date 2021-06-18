#quit all the other bars
killall -q polybar 



#wait for them to close 
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done 

#launch bars
polybar example -r &
