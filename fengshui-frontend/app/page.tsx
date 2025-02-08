import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Separator } from "@/components/ui/separator"
import { Progress } from "@/components/ui/progress"

const zodiacData = {
  reading: {
    gregorian_calendar: "03/01/1994 08:15",
    gregorian_lunar_calendar: "01/19/1994 08:15",
    lunar_calendar: "一月十九 甲戌",
    zodiac: "Wood Dog",
    good_luck_colors_for_this_year: ["Green", "Brown", "Gold"],
    bad_luck_colors_for_this_year: ["Red", "Black"],
    good_aspects: [
      {
        aspect: "Harmonious relationships",
        short_reason: "Strong social connections foster mutual support.",
      },
      {
        aspect: "Career advancement",
        short_reason: "Opportunities for growth and recognition in the workplace.",
      },
      {
        aspect: "Financial stability",
        short_reason: "Smart investments yield positive returns.",
      },
      {
        aspect: "Health improvements",
        short_reason: "Increase in energy and well-being this year.",
      },
      {
        aspect: "Personal development",
        short_reason: "Focus on self-growth leads to new insights.",
      },
    ],
    bad_aspects: [
      {
        aspect: "Relationship conflicts",
        short_reason: "Miscommunication may lead to misunderstandings.",
      },
      {
        aspect: "Work-related stress",
        short_reason: "Increased workload may cause pressure.",
      },
      {
        aspect: "Health concerns",
        short_reason: "Potential for seasonal illnesses.",
      },
      {
        aspect: "Financial risks",
        short_reason: "Be cautious with new ventures.",
      },
      {
        aspect: "Travel complications",
        short_reason: "Possible delays or disruptions in travel plans.",
      },
    ],
  },
}

export default function ZodiacReading() {
  const { reading } = zodiacData

  return (
    <Card className="w-full max-w-4xl mx-auto">
      <CardHeader>
        <CardTitle className="text-3xl font-bold text-center">The Year of the Snake</CardTitle>
        <p className="text-center mt-1">commencing on January 29, 2025, is characterized by wisdom, transformation, and adaptability. Associated with intelligence and strategic thinking, this year encourages personal growth and careful decision-making. The Wood element introduces flexibility and creativity, promoting deeper reflection and thoughtful planning. Embracing change and long-term strategies will be beneficial during this period. Overall, the Year of the Snake emphasizes introspection and deliberate action.</p>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h2 className="text-2xl font-semibold mb-4">Basic Information</h2>
            <p>
              <strong>Gregorian Calendar:</strong> {reading.gregorian_calendar}
            </p>
            <p>
              <strong>Gregorian Lunar Calendar:</strong> {reading.gregorian_lunar_calendar}
            </p>
            <p>
              <strong>Lunar Calendar:</strong> {reading.lunar_calendar}
            </p>
            <p>
              <strong>Zodiac:</strong> {reading.zodiac}
            </p>
          </div>
          <div>
            <h2 className="text-2xl font-semibold mb-4">Lucky Colors</h2>
            <div className="flex flex-wrap gap-2 mb-2">
              {reading.good_luck_colors_for_this_year.map((color) => (
                <Badge key={color} variant="outline" className="text-green-600 border-green-600">
                  {color}
                </Badge>
              ))}
            </div>
            <h2 className="text-2xl font-semibold mb-2 mt-4">Unlucky Colors</h2>
            <div className="flex flex-wrap gap-2">
              {reading.bad_luck_colors_for_this_year.map((color) => (
                <Badge key={color} variant="outline" className="text-red-600 border-red-600">
                  {color}
                </Badge>
              ))}
            </div>
          </div>
        </div>

        <Separator className="my-6" />
        <div className="grid grid-cols-1 gap-6">
          <div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h2 className="text-2xl font-semibold mb-4">Positive Aspects</h2>
                {reading.good_aspects.map((aspect, index) => (
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
                {reading.bad_aspects.map((aspect, index) => (
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
      </CardContent>
    </Card>
  )
}

