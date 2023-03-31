#$aaa = 10; 멀티 프로세스라서 여기서 변수를 선언해도 아래 함수는 서브 프로세스로 띄웠으므로 사용 불가능
#multi_pro~ 만 fork 한 것임. (전체 포크 시 함수로 전체를 감싸거나 그 외...(?)
function multi_processing(){
    for i in {1..5}; do
        echo $i
        sleep 3
    done
}

multi_processing &

for i in {6..10}; do
    echo $i
    sleep 3
done
