import RequestHTML as req
import ReviewFinder as rev

if __name__ == "__main__":
    response_html = req.RequestAuto('html_content', 'https://www.amazon.com/Under-Armour-Charged-Assert-Running/dp/B09XBVT7WX/?_encoding=UTF8&pd_rd_w=hja1j&content-id=amzn1.sym.4b90c80a-3aee-44a3-b41d-fc2674a3ef63%3Aamzn1.symc.ee4c414f-039b-458d-a009-4479557ca47b&pf_rd_p=4b90c80a-3aee-44a3-b41d-fc2674a3ef63&pf_rd_r=4G4HCCNW4WQWZ084NBKP&pd_rd_wg=RvAtp&pd_rd_r=447c9b1d-5628-49b9-aeac-ac6ee11b237e&ref_=pd_hp_d_btf_ci_mcx_mr_hp_d')
    
    detective = rev.DetectiveNLP(response_html)

    detective.get_nlp()

   