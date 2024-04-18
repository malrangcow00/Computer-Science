### 연계 메커니즘
- 응용 소프트웨어와 연계 대상 모듈 간의 데이터 연계 시 요구사항을 고려한 연계방법과 주기를 설계하기 위한 메커니즘
- 데이터를 생성하여 전송하는 송신 시스템과 송신 데이터를 수신하여 DB에 반영하는 수신 시스템으로 구성

<table>
<tr>
<th>분류</th>
<th>설명</th>
</tr>
<tr>
<td>직접 연계 방식</td>
<td>구성 요소들이 직접적으로 서로 연결되어 있는 방식</td>
</tr>
<tr>
<td>간접 연계 방식</td>
<td>중간 매개체를 통해 구성 요소들이 통신하는 방식</td>
</tr>
</table>

<table>
<tr>
<th>구분</th>
<th>연계 기술</th>
<th>설명</th>
</tr>
<tr>
<td rowspan="4">간접 연계</td>
<td>EAI<br>
(Enterprise Application Integration)</td>
<td>- 기업에서 운영되는 서로 다른 플랫폼 및 애플리케이션들 간의 정보 전달, 연계, 통합을 가능하게 해주는 솔루션<br>
- 송수신 시스템에 설치되는 어댑터를 이용하는 기술</td>
</tr>
<tr>
<td>ESB<br>
(Enterprise Service Bus)</td>
<td>기업에서 운영되는 서로 다른 플랫폼 및 애플리케이션들 간을 하나의 시스템으로 관리 운영할 수 있도록 서비스 중심의 통합을 지향하는 아키텍처</td>
</tr>
<tr>
<td>웹 서비스<br>
(Web Service)</td>
<td>- 네트워크에 분산된 정보를 서비스 형태로 개방하여 표준화된 방식<br>
- 웹 서비스가 설명된 <a href="wsdl_and_soap.md">WSDL과 SOAP 프로토콜</a>을 이용한 시스템 간 연계</td></tr>
<tr>
<td>소켓<br>
(Socket)</td>
<td>소켓을 생성하여 포트를 할당하고, 클라이언트의 요청을 연결하여 통신하는 기술<br>
ex. TcpServer.listen();</td></tr>
<tr>
<td rowspan="5">직접 연계</td>
<td>DB 링크<br>
(DB Link)</td>
<td>- 데이터베이스에서 제공하는 DB 링크 객체를 이용하는 기술<br>
- 수신 시스템에서 DB 링크를 생성하고 송신 시스템에서 해당 DB 링크를 직접 참조하는 방식<br>
ex. 테이블명@DBLink명</td></tr>
<tr><td>DB 연결<br>
(DB Connection)</td>
<td>수신 시스템의 WAS에서 송신 시스템 DB로 연결하는 DB 커넥션 풀(DB Connection Pool)을 생성하고 연계 프로그램에서 해당 DB 커넥션 풀 명을 이용하여 연결하는 기술<br>
ex. 송신 시스템의 Data Source = DB Connection Pool 이름</td></tr>
<tr><td>API/Open API</td>
<td>- 송신 시스템의 DB에서 데이터를 읽어서 제공하는 애플리케이션 프로그래밍 인터페이스 프로그램<br>
- API명, 입출력 파라미터 정보가 필요</td></tr>
<tr><td>JDBC</td>
<td>- 수신 시스템의 프로그램에서 JDBC 드라이버를 이용하여 송신 시스템 DB와 연결하는 기술<br>
- DBMS 유형, DBMS 서버 IP와 Port, DB <a href="instance.md">인스턴스</a> 정보가 필요</td></tr>
<tr>
<td>하이퍼 링크<br>
(Hyper Link)</td>
<td>현재 페이지에서 다른 부분으로 가거나 전혀 다른 페이지로 이동하게 해주는 속성<br>
<xmp>ex. <a href="url"> Link 대상 </a></xmp></td></tr>
</table>
