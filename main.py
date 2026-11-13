# main.py

def categorize_request_simple(message: str) -> str:
    """
    Categorizes a customer support message using simple keyword matching.
    This demonstrates a 'simple automation' approach, as advocated by the article,
    over potentially over-engineered AI solutions.
    """
    message_lower = message.lower()

    # Simple rule-based logic for categorization.
    # For many common tasks, this approach is fast, predictable, and requires
    # no training data, complex models, or expensive inference, making it
    # more efficient and reliable than an AI agent.
    if any(keyword in message_lower for keyword in ["hesap", "fatura", "ödeme", "abonelik"]):
        return "Fatura ve Hesap Sorgusu" # Billing and Account Inquiry
    elif any(keyword in message_lower for keyword in ["hata", "çalışmıyor", "problem", "teknik", "kurulum"]):
        return "Teknik Destek" # Technical Support
    elif any(keyword in message_lower for keyword in ["yeni özellik", "istek", "geliştirme", "öneri"]):
        return "Özellik Talebi" # Feature Request
    elif any(keyword in message_lower for keyword in ["iade", "iptal", "geri ödeme"]):
        return "İade/İptal İşlemleri" # Refund/Cancellation Procedures
    else:
        return "Genel Sorgu" # General Inquiry

def main():
    customer_messages = [
        "Faturamda bir yanlışlık var, kontrol edebilir misiniz?",
        "Uygulama sürekli çöküyor, teknik destek alabilir miyim?",
        "Yeni bir özellik olarak 'karanlık mod' eklemenizi rica ediyorum.",
        "Hesabımı nasıl iptal edebilirim?",
        "Ürün hakkında daha fazla bilgi almak istiyorum.",
        "Ödemem neden başarısız oldu?",
        "Şifremi unuttum ve sıfırlayamıyorum.",
        "Geri ödeme talebim ne durumda?"
    ]

    print("--- Basit Otomasyon ile Müşteri Mesajı Kategorizasyonu ---")
    print("Makalenin vurguladığı gibi, basit kurallara dayalı otomasyonlar,")
    print("birçok durumda karmaşık YZ ajanlarından daha hızlı, ekonomik ve güvenilirdir.\n")

    for i, message in enumerate(customer_messages):
        # This simple function effectively categorizes messages without the overhead
        # of an AI model (data collection, training, inference costs, maintenance).
        category = categorize_request_simple(message)
        print(f"Mesaj {i+1}: \"{message}\"")
        print(f"Kategori: {category}\n")

    print("--- Neden Basit Otomasyon? ---")
    print("Bu örnekte, anahtar kelime tabanlı basit bir mantık, müşteri taleplerini")
    print("doğru bir şekilde sınıflandırmak için yeterlidir. Bir YZ NLP modeli")
    print("geliştirmek, eğitmek ve dağıtmak çok daha fazla zaman, kaynak ve uzmanlık")
    print("gerektirecektir. Çoğu zaman, 'iyi yeterlidir' prensibiyle hareket etmek")
    print("daha akıllıca bir yaklaşımdır.")

if __name__ == "__main__":
    main()
