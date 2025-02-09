
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";

interface FengShui {
  gregorian_calendar?: string;
  gregorian_lunar_calendar?: string;
  lunar_calendar?: string;
  zodiac?: string;
  zodiac_vs_this_year?: string;
  good_luck_colors_for_this_year?: string[];
  bad_luck_colors_for_this_year?: string[];
  good_aspects?: {
    aspect: string;
    short_reason: string;
  }[];
  bad_aspects?: {
    aspect: string;
    short_reason: string;
  }[];
  business_advise?: string;
  relationship_advise?: string;
  life_advise?: string;
}

export default function FengShuiResults({ fengShui }: { fengShui: FengShui }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-2xl font-semibold mb-4">Zodiac vs This Year</CardTitle>
        <p>{fengShui.zodiac_vs_this_year || "N/A"}</p>
      </CardHeader>
      <CardContent>
        <p>
          <strong>Gregorian Calendar:</strong> {fengShui?.gregorian_calendar || "N/A"}
        </p>
        <p>
          <strong>Gregorian Lunar Calendar:</strong> {fengShui?.gregorian_lunar_calendar || "N/A"}
        </p>
        <p>
          <strong>Lunar Calendar:</strong> {fengShui?.lunar_calendar || "N/A"}
        </p>
        <p>
          <strong>Zodiac:</strong> {fengShui?.zodiac || "N/A"}
        </p>

      <h2 className="text-2xl font-semibold mb-4">Lucky Colors</h2>
      <div className="flex flex-wrap gap-2 mb-2">
          {fengShui.good_luck_colors_for_this_year?.map((color) => (
          <Badge key={color} variant="outline" className="text-green-600 border-green-600">
              {color}
          </Badge>
          ))}
      </div>
      <h2 className="text-2xl font-semibold mb-2 mt-4">Unlucky Colors</h2>
      <div className="flex flex-wrap gap-2">
          {fengShui.bad_luck_colors_for_this_year?.map((color) => (
          <Badge key={color} variant="outline" className="text-red-600 border-red-600">
              {color}
          </Badge>
          ))}
      </div>

      <Separator className="my-6" />

      <div className="grid grid-cols-1 gap-6">
          <div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
              <h2 className="text-2xl font-semibold mb-4">Positive Aspects</h2>
              {fengShui.good_aspects?.map((aspect, index) => (
                  <div key={index} className="mb-4">
                  <div className="flex justify-between items-center mb-2">
                      <span className="font-semibold">{aspect.aspect}</span>
                  </div>
                  <p className="text-sm text-muted-foreground">{aspect.short_reason}</p>
                  </div>
              ))}
              </div>
              <div>
              <h2 className="text-2xl font-semibold mb-4">Challenging Aspects</h2>
              {fengShui.bad_aspects?.map((aspect, index) => (
                  <div key={index} className="mb-4">
                  <div className="flex justify-between items-center mb-2">
                      <span className="font-semibold">{aspect.aspect}</span>
                  </div>
                  <p className="text-sm text-muted-foreground">{aspect.short_reason}</p>
                  </div>
              ))}
              </div>
          </div>
          </div>
      </div>

      <Separator className="my-6" />
      <h2 className="text-2xl font-semibold mb-4">Business Advice</h2>
      <p className="text-sm text-muted-foreground">{fengShui?.business_advise || "N/A"}</p>
      
      <Separator className="my-6" />
      <h2 className="text-2xl font-semibold mb-4">Relationship Advice</h2>
      <p className="text-sm text-muted-foreground">{fengShui?.relationship_advise || "N/A"}</p>
      
      <Separator className="my-6" />
      <h2 className="text-2xl font-semibold mb-4">Life Advice</h2>
      <p className="text-sm text-muted-foreground">{fengShui?.life_advise || "N/A"}</p>
      </CardContent>
    </Card>
  );
}
