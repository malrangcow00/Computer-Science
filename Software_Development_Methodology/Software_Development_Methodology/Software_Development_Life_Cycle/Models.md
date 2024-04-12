### 소프트웨어 생명주기 모델의 종류
<table>
    <tr>
        <th>종류</th>
        <th colspan="2">설명</th>
    </tr>
    <tr>
        <td rowspan="2">
            <a href="Software_Development_Life_Cycle_Models/Waterfall-Model.md">
            폭포수 모델<br>
            (Waterfall Model)
            </a>
        </td>
        <td colspan="2">- 소프트웨어 개발 시 각 단계를 확실히 마무리 지은 후에 다음 단계로 넘어가는 모델<br>
            - 모형의 적용 경험과 성공 사례가 많음<br>
            - 단계별 정의와 산출물이 명확하다
        </td>
    </tr>
    <tr>
        <td>절차</td>
        <td>타당성 검토 &rarr; 계획 &rarr; 요구사항 분석 &rarr; 설계 &rarr; 구현(코딩) &rarr; 테스트(검사) &rarr; 유지보수</td>
    </tr>
    <tr>
        <td>프로토타이핑 모델<br>
            (Prototyping Model)
        </td>
        <td colspan="2">고객이 요구한 주요 기능을 프로토타입으로 구현하여, 고객의 피드백을 반영하여 소프트웨어를 만들어가는 모델</td>
    </tr>
    <tr>
        <td rowspan="2"><a href="Software_Development_Life_Cycle_Models/Spiral-Model.md">
            나선형 모델<br>
            (Spiral Model)</a>
        </td>
        <td colspan="2">시스템 개발 시 위험을 최소화하기 위해 점진적으로 완벽한 시스템으로 개발해 나가는 모델</td>
    </tr>
    <tr>
        <td>절차</td>
        <td>계획 및 정의 &rarr; 위험 분석 &rarr; 개발 &rarr; 고객 평가</td>
    </tr>
    <tr>
        <td>반복적 모델<br>
            (Iteration Model)
        </td>
        <td colspan="2">- 구축대상을 나누어 병렬적으로 개발 후 통합하거나, 반복적으로 개발하여 점증 완성시키는 SDLC 모델<br>
            - 사용자의 요구사항 일부분 혹은 제ㅐ품 일부분을 반복적으로 개발하여 최종 시스템으로 완성하는 모델
        </td>
    </tr>
</table>

### 소프트웨어 생명주기 모델 간 비교
<table>
    <tr>
        <th>구분</th>
        <th>폭포수 모델</th>
        <th>프로토타이핑 모델</th>
        <th>나선형 모델</th>
        <th>반복적 모델</th>
    </tr>
    <tr>
        <td>절차도</td>
        <td>요구사항 분석 &rarr; 설계 &rarr; 구현 &rarr; 테스트</td>
        <td>요구사항 분석 &rarr; 프로토타입 개발 &rarr; 프로토타입 평가 (평가 탈락 시 다시 요구사항 분석으로 이동) &rarr; 구현 &rarr; 테스트</td>
        <td>계획 및 정의 &rarr; 위험분석 &rarr; 개발 &rarr; 고객평가 (평가 탈락 시 다시 계획 및 정의로 이동)</td>
        <td>개발 대상(1) : 분석(N) &rarr; 설계  &rarr; 구현</td>
    </tr>
    <tr>
        <td>특징</td>
        <td>순차적 접근</td>
        <td>프로토타입 개발</td>
        <td>위험분석, 반복 개발</td>
        <td>증분방식으로 병행 개발</td>
    </tr>
    <tr>
        <td>장점</td>
        <td>이해가 용이<br>관리가 편리</td>
        <td>요구분석 용이<br>타당성 검증 가능</td>
        <td><strong>위험성 감소</strong>와 변경에 유연한 대처</td>
        <td>병행 개발로 인한 일정 단축 가능</td>
    </tr>
    <tr>
        <td>단점</td>
        <td>요구사항 변경이 어려움</td>
        <td>프로토타입 폐기에 따른 비용 증가</td>
        <td>단계 반복에 따른 관리 어려움</td>
        <td>병행 개발에 따른 관리 비용 증가</td>
    </tr>
</table>