Title: การเอาคำที่ตัดได้จาก Lucene Analyzer 
Date: 2009-09-26 10:38:12
Tags: lucene, nlp 
Slug: การเอาคำที่ตัดได้จาก Lucene Analyzer 


มีผู้อ่านท่านหนึ่งถามมาว่าจะเอาคำที่ตัดได้จาก Analyzer ของ Lucene ไปใช้ได้อย่างไร จากการลองซักพักหนึ่งทำให้ได้วิธีมาดังนี้ครับ

	:::Java

	import java.io.IOException;
	import java.io.StringReader;
	import org.apache.lucene.analysis.Analyzer;
	import org.apache.lucene.analysis.Token;
	import org.apache.lucene.analysis.TokenStream;
	import org.apache.lucene.analysis.th.ThaiAnalyzer;

	/**
	 * Demonstrate how to obtain a list of Lucene tokens.
	 * @author Wittawat Jitkrittum (Sep 26, 2009)
	 */
	public class TestLuceneAnalyzer {

	public static void tokenize(Analyzer analyzer, String text) throws IOException{
	// เรียก method ชื่อ tokenStream เพื่อให้ได้สายของ token มา argument แรกเป็นชื่อ field ใน
	// document ของ Lucene ในที่นี้เราไม่ได้ใช้ ก็ไม่ต้องสนใจ
	TokenStream ts = analyzer.tokenStream(null, new StringReader(text));
	// สร้าง Token ไว้เก็บผลลัพธ์ของคำที่ได้มา
	Token token  = new Token();
	// วน loop เพื่อเอา token ทีละอันจาก TokenStream เหตุที่ใส่ token เป็น argument ไปให้ด้วย
	// เข้าใจว่าอยากให้เร็วจะได้ไม่ต้องสร้างอันใหม่
	while((token = ts.next(token)) != null){
	String term = token.term(); //เรียก method term() บน token เพื่อเอาคำเป็น String
	System.out.print(term);
	System.out.print(" | ");
	}
	System.out.println();
	}
	public static void main(String[] args) throws Exception{
	Analyzer thaiAnalyzer = new ThaiAnalyzer();
	String text = "นี่คือประโยคเอาไว้ทดสอบการตัดคำของ Lucene Analyzer";
	tokenize(thaiAnalyzer, text);
	}
	}


พอรัน main ด้านบนก็จะได้ประมาณนี้ครับ

นี่ | คือ | ประโยค | เอา | ไว้ | ทดสอบ | การ | ตัด | คำ | ของ | lucene | analyzer |

สำหรับคนที่อยากรู้เรื่องการทำ index โดยใช้ Lucene ขอเชิญ<a title="Thai Text Search with Lucene" href="http://wittawat.com/blog/?p=47">คลิกอ่าน post อันเก่านี้</a> เขียนจบแล้วเพิ่งนึกได้ว่าผู้ที่ถามมาอาจจะอยากเข้าถึงคำที่อยู่ใน index รึป่าว.. ไม่ใช่เอา Analyzer มาใช้เฉยๆแบบนี้ ถ้ากรณีนั้นเอาไว้มีเวลาจะเขียนทีหลังครับ
