PNOS=(
	10250
	10809
	1152
	2439
	2577
	2884
	2920
	3052
	31403
	8958
)

for PNO in "${PNOS[@]}"; do
	echo "$PNO"
	git add "$PNO"
	git commit -m "boj/$PNO"
done
