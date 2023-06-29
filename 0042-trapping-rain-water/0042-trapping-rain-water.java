class Solution {
    public int trap(int[] height) {
        int answer = 0;
        for (int i = 0; i < height.length; i++) {
            if (height[i] > 0) {
                for (int j = i; j < height.length - 1; j++) {
                    for (int k = j + 1; k < height.length; k++) {
                        if (height[j] <= height[j + 1]) {
                            break;
                        }
                        else if (height[j] <= height[k] && (k - j) > 1) {
                            answer += (k - j - 1) * height[j];
                            System.out.println(answer);
                            for (int l = j + 1; l < k; l++) {
                                answer -= height[l];
                                System.out.println(answer);
                            }
                            j = k - 1;
                            
                            break;
                        }
                        // 만약에 기준이 되는 애가 max면 그 뒤에서 max인 애를 찾고 걔를 기준으로 !!
                        else {
                            int max = height[j];
                            for (int l = j + 1; l < height.length; l++) {
                                if (height[l] > max) {
                                    max = height[l];
                                }
                            }
                            if (max == height[j]) {
                                int max2 = height[j + 1];
                                int maxIdx = j + 1;
                                for (int l = j + 1; l < height.length; l++) {
                                    if (max2 < height[l]) {
                                        max2 = height[l];
                                        maxIdx = l;
                                    }
                                }
                                height[j] = max2;
                                answer += (maxIdx - j - 1) * height[j];
                                System.out.println(answer);
                                for (int l = j + 1; l < maxIdx; l++) {
                                    answer -= height[l];
                                    System.out.println(answer);
                                }
                                j = maxIdx - 1;
                                System.out.println(answer);
                                break;
                            }
                        }
                    }
                }
                break;
            }
        }
        if (answer < 0)
            return 0;
        return answer;
    }
}